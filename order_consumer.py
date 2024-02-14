# sourcery skip: convert-to-enumerate
from kafka import KafkaConsumer
import json
import constants


consumer = KafkaConsumer(
    constants.ORDER_CREATED_TOPIC, bootstrap_servers=constants.BOOTSTRAP_SERVER
)

print("Gonna start listening")
while True:
    i = 1
    for message in consumer:
        print(f"Order #{i} received: {json.loads(message.value.decode('utf-8'))}")
        i += 1
        print()
