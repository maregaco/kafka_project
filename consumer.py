from confluent_kafka import Consumer, KafkaError
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-workers',
    'auto.offset.reset': 'earliest' #to receive all messages from the beginning of the topic
})
consumer.subscribe(['orders'])
totals = {}

while True:
    message = consumer.poll(1.0)

    if message is None:
        continue

    if message.error() is not None:
        if message.error().code() == KafkaError._PARTITION_EOF:
            continue
        print(message.error())
        break

    order = json.loads(message.value().decode('utf-8'))
    customer_id = order['customer_id']
    if customer_id in totals:
        totals[customer_id] += order['amount']
    else:
        totals[customer_id] = order['amount']
    print(f"Customer: {customer_id}, Total Amount: {totals[customer_id]}")
    print(f"Partition: {message.partition()}")
    