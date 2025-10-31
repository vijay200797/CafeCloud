
from rabbit_mq import listen_to_orders_created


if __name__=="__main__":
    while True:
        listen_to_orders_created()