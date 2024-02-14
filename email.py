import json

from confluent_kafka import Consumer
import constants

config = consumer_conf = {
    "bootstrap.servers": constants.BOOTSTRAP_SERVER,
    "group.id": "my_consumer_group",
    "auto.offset.reset": "earliest",
}
consumer = Consumer(consumer_conf)
consumer.subscribe([constants.ORDER_CONFIRMED_TOPIC])

emails_sent_so_far = set()
print("Gonna start listening")
while True:
    msg = consumer.poll(constants.CONSUMER_POLLING_INTERVAL)
    if not msg:
        continue
    consumed_message = json.loads(msg.value().decode())
    customer_email = consumed_message["customer_email"]
    print(f"Sending email to : {customer_email} ")
    emails_sent_so_far.add(customer_email)
    print(f"Emails sent so far: {len(emails_sent_so_far)}")
    print()
