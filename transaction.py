import json

from kafka import KafkaConsumer
from kafka import KafkaProducer
import constants

consumer = KafkaConsumer(
    constants.ORDER_CREATED_TOPIC, bootstrap_servers=constants.BOOTSTRAP_SERVER
)
producer = KafkaProducer(bootstrap_servers=constants.BOOTSTRAP_SERVER)


print("Gonna start listening")
i = 1
while True:
    for message in consumer:
        print(f"Ongoing transaction #{i}")
        consumed_message = json.loads(message.value.decode())
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
        producer.send(constants.ORDER_CONFIRMED_TOPIC, json.dumps(data).encode("utf-8"))
