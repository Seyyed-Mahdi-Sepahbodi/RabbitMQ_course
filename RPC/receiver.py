import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def callback(ch, method, properties, body):
    n = int(body)
    print(f'Processing message')
    time.sleep(4)
    response = str(n + 1)
    channel.basic_publish(exchange='', routing_key=properties.reply_to, body=response, properties=pika.BasicProperties(correlation_id=properties.correlation_id))
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=callback)
print('Waiting for messages')
channel.start_consuming()