import json
import time
import constants
from confluent_kafka import Producer

config = {"bootstrap.servers": constants.BOOTSTRAP_SERVER}
producer = Producer(config)

print(f"Will generate one unique order every {constants.SLEEP_FOR} seconds")

for i in range(1, constants.ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i * 5,
        "items": "burger,sandwich",
    }

    producer.produce(
        topic=constants.ORDER_CREATED_TOPIC,
        value=json.dumps(data).encode("utf-8"),
    )
    print(f"Done Sending..{i}")
    time.sleep(constants.SLEEP_FOR)
