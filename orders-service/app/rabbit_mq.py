import pika
import json
from config import settings


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


def publish_order_created(order_data):
    connection, channel = __get_connection()

    exchange_name = 'orders_exchange'
    routing_key = 'orders.created'

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)
    print("Data Received")
    print(order_data)
    message_body = json.dumps(order_data.to_dict())
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