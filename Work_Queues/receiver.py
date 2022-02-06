import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='First', durable=True)
pirnt('Waiting for message, press ctrl+c to exit')


def callback(ch, method, properties, body):
    print(f'Received {body}')
    time.sleep(9)
    print('Done')
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='First', on_message_callback=callback)

channel.start_consuming()