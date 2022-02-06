import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='Hello')

channel.basic_publish(exchange='', routing_key='Hello', body='Hello World')

print('Message Sent')

connection.close()