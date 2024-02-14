import json

from kafka import KafkaConsumer
import constants


consumer = KafkaConsumer(
    constants.ORDER_CONFIRMED_TOPIC, bootstrap_servers=constants.BOOTSTRAP_SERVER
)

emails_sent_so_far = set()
print("Gonna start listening")
while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        print(f"Sending email to : {customer_email} ")
        emails_sent_so_far.add(customer_email)
        print(f"Emails sent so far: {len(emails_sent_so_far)}")
        print()
