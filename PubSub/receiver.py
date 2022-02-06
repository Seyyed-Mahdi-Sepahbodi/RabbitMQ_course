import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue

channel.queue_bind(queue=queue_name, exchange='logs')
print('Waiting for logs')


def callback(ch, method, properties, body):
    print(f'Received {body}')
    print(queue_name)

channel.basic_consume(queue=queue_name, on_message_callback=callback)

channel.start_consuming()