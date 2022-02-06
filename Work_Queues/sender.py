import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='First', durable=True)

message = 'This is a testing message'

channel.basic_publish(exchange='', routing_key='First', properties=pika.BasicProperties(delivery_mode=2))


connection.close()



