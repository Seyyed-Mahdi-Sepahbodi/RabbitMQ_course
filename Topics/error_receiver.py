import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue

binding_key = '#.important'
channel.queue_bind(queue=queue_name, exchange='topic_logs', routing_key=binding_key)

print('Waiting for messages')

def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(f'{body} \n')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
