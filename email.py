import json

from confluent_kafka import Consumer
import constants

consumer_conf = {
    "bootstrap.servers": constants.BOOTSTRAP_SERVER,
    "group.id": "email_consumer_id",
    "auto.offset.reset": "earliest",
}
consumer = Consumer(consumer_conf)
consumer.subscribe([constants.ORDER_CONFIRMED_TOPIC])

print("Gonna start listening")
i = 1
while True:
    msg = consumer.poll(constants.CONSUMER_POLLING_INTERVAL)
    if not msg:
        continue
    consumed_message = json.loads(msg.value().decode())
    customer_email = consumed_message["customer_email"]
    print(f"Sending email to : {customer_email} ")
    print(f"Emails sent so far: {i}")
    print()
    i += 1
