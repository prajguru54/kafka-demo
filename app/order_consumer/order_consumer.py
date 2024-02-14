# sourcery skip: convert-to-enumerate
from confluent_kafka import Consumer
import json
from app.core import constants
from app.order_consumer.order import Order

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
    order_data = json.loads(msg.value().decode("utf-8"))
    print(f"Order #{i} received: {order_data}")
    order = Order(user_id="", total_cost="")
    i += 1
    print()
