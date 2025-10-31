import pika
import json
from config import settings
import time
import requests


RABBIT_MQ_SERVER = settings.rabbit_mq_server
RABBIT_MQ_PORT = settings.rabbit_mq_port
RABBIT_MQ_USER = settings.rabbit_mq_user
RABBIT_MQ_PASSWORD = settings.rabbit_mq_password

def __get_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBIT_MQ_SERVER,  
            port=RABBIT_MQ_PORT,
            credentials=pika.PlainCredentials(RABBIT_MQ_USER, RABBIT_MQ_PASSWORD)
        )
    )
    channel = connection.channel()
    return connection, channel


def publish_order_completed(order_data):
    connection, channel = __get_connection()

    exchange_name = 'orders_exchange'
    routing_key = 'orders.completed'

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

    message_body = json.dumps(order_data)
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message_body,
        properties=pika.BasicProperties(
            delivery_mode=2  
        )
    )

    print(f" [x] Sent message on topic '{routing_key}': {message_body}")
    connection.close()

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f" [x] Received message on {method.routing_key}: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

    time.sleep(4)
    URL = settings.api_url + "Order/"+ str(data["orderid"])
    print("Sending Request to complete order To API " +  URL) 
    HEADERS ={'content-Type': 'application/json'}
    response = requests.put(url=URL, data= data, headers=HEADERS)
    rvalue = response.json()
    if rvalue['status'] == "C":
        data["status"] = "C"
        publish_order_completed(data)
    else:
        print("Failed to Marked Completed Order")

def listen_to_orders_created():
    connection, channel = __get_connection()

    exchange_name = 'orders_exchange'
    routing_key = 'orders.created'

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    print(f" [*] Waiting for messages on topic '{routing_key}'. To exit press CTRL+C")

    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()