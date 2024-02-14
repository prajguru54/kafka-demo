import json

from confluent_kafka import Consumer
import constants

config = consumer_conf = {
    "bootstrap.servers": constants.BOOTSTRAP_SERVER,
    "group.id": "my_consumer_group",
    "auto.offset.reset": "earliest",
}
consumer = Consumer(config)
consumer.subscribe([constants.ORDER_CONFIRMED_TOPIC])

total_orders_count = 0
total_revenue = 0
print("Gonna start listening")
while True:
    msg = consumer.poll(constants.CONSUMER_POLLING_INTERVAL)
    if not msg:
        continue
    print("Updating analytics..")
    consumed_message = json.loads(msg.value().decode())
    total_cost = float(consumed_message["total_cost"])
    total_orders_count += 1
    total_revenue += total_cost
    print(f"Orders so far today: {total_orders_count}")
    print(f"Revenue so far today: {total_revenue}")
