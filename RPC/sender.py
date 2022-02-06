import pika
import uuid


class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        queue = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = queue.method.queue
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_response, auto_ack=True)

    def on_response(self, ch, method, properties, body):
        if self.correlation_id == properties.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        send.channel.basic_publish(
            exchange='', 
            routing_key='rpc_queue', 
            body=str(n),
            properties=pika.BasicProperties(reply_to=self.queue_name, correlation_id=self.correlation_id))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

send = Sender()
response = send.call(30)

print(response)