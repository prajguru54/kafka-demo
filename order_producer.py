import json
import time
import constants

from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=constants.BOOTSTRAP_SERVER)

print(f"Will generate one unique order every {constants.SLEEP_FOR} seconds")

for i in range(1, constants.ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i * 5,
        "items": "burger,sandwich",
    }

    producer.send(constants.ORDER_CREATED_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(constants.SLEEP_FOR)
