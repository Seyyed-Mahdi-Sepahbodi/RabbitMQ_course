import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

messages = {
    'error.warning.important':'This is an important message',
    'info.debug.notimportant':'This is not an important message'
}

for k,v in messages.items():
    channel.basic_publish(exchange='topic_logs', routing_key=k, body=v)
    
print('Sent message')

connection.close()