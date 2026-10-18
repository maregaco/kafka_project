from confluent_kafka import Producer
import json

producer = Producer({'bootstrap.servers': 'localhost:9092'})

''' For testing purposes, we can send messages to Kafka in a loop. In a real application, you would likely have a more complex logic for producing messages.
while True:
    message = input("Enter a message to send to Kafka (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    producer.produce('test', value=message)
    producer.flush()
    print(f"Sent: {message}")
'''
for i in range(100):
    order = {
        'order_id': i,
        'customer_id': i%100,
        'amount': i*100
    }

    producer.produce('orders', key=str(order['order_id']), value=json.dumps(order))
    producer.flush()