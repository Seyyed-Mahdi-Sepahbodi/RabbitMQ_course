import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue

severity = 'error'

channel.queue_bind(queue=queue_name, exchange='direct_logs', routing_key=severity)
print('Waiting for message')

def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(str(body) + '\n')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()