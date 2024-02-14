# sourcery skip: convert-to-enumerate
from confluent_kafka import Consumer
import json
import constants

config = {
    "bootstrap.servers": constants.BOOTSTRAP_SERVER,
    "group.id": "order_processor_consumer_id",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(config)
consumer.subscribe([constants.ORDER_CREATED_TOPIC])

print("Gonna start listening")
i = 1
while True:
    msg = consumer.poll(timeout=constants.CONSUMER_POLLING_INTERVAL)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    print(f"Order #{i} received: {json.loads(msg.value().decode('utf-8'))}")
    i += 1
    print()
