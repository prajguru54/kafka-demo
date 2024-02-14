ORDER_CREATED_TOPIC = "order_details"
ORDER_CONFIRMED_TOPIC = "order_confirmed"

BOOTSTRAP_SERVER = "localhost:29092"


ORDER_LIMIT = 100  # Produce maximum these many orders
SLEEP_FOR = 5  # Produce orders after every specified seconds
CONSUMER_POLLING_INTERVAL = 1  # polls for incoming messages
