# kafka-demo
This is a simple project to demonstrate the usage of kafka using python

# Local Project setup
1. pip install virtualenv
2. virtualenv env
3. source ./env/bin/activate
4. pip install -r requirements.txt
5. docker-compose up
6. python -m app.order_producer.order_producer
7. python -m app.order_consumer.order_consumer
8. python -m app.transaction.transaction
9. python -m app.email.email.py
10. python -m app.analytics.analytics.py

#### Note: run step 6-10 in seperate terminals, simultaneously
