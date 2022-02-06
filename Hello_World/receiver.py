import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='Hello')

def callback(ch, method, properties, body):
    print(f'Received {body}')

channel.basic_consume(queue='Hello', on_message_callback=callback, auto_ack=True)


channel.start_consuming()

