import json

from confluent_kafka import Producer, Consumer
from app.core import constants

consumer_conf = {
    "bootstrap.servers": constants.BOOTSTRAP_SERVER,
    "group.id": "transaction_consumer_id",
    "auto.offset.reset": "earliest",
}
consumer = Consumer(consumer_conf)
consumer.subscribe([constants.ORDER_CREATED_TOPIC])

producer_conf = {"bootstrap.servers": constants.BOOTSTRAP_SERVER}
producer = Producer(producer_conf)


print("Gonna start listening")
i = 1
while True:
    msg = consumer.poll(constants.CONSUMER_POLLING_INTERVAL)
    if not msg:
        continue
    print(f"Ongoing transaction #{i}")
    consumed_message = json.loads(msg.value().decode())
    # print(consumed_message)
    user_id = consumed_message["user_id"]
    print(f"user_id: {user_id}")
    total_cost = consumed_message["total_cost"]
    data = {
        "customer_id": user_id,
        "customer_email": f"{user_id}@gmail.com",
        "total_cost": total_cost,
    }
    print(f"Successful transaction #{i}")
    i += 1
    print()
    producer.produce(
        topic=constants.ORDER_CONFIRMED_TOPIC,
        value=json.dumps(data).encode("utf-8"),
    )
