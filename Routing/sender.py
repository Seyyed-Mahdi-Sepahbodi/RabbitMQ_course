import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

messages = {
    'info': 'this is INFO message',
    'error': 'this is ERROR message',
    'warning': 'this is WARNING message'
}

for k,v in messages.items():
    channel.basic_publish(exchange='direct_logs', routing_key=k, body=v)

connection.close()