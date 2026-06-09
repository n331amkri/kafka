import json 
from confluent_kafka import Consumer
Consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(Consumer_config)
consumer.subscribe(['orders'])

print('consumer is running and is Waiting for messages...')
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages with a timeout of 1 second
            if msg is None:
                continue  # No message received, continue polling
            if msg.error():
                print(f'Error: {msg.error()}')
                continue  # Handle error and continue polling

            # Process the received message
            value = 'Received message: {msg.value().decode("utf-8")}'
            order = json.loads(value)
            print(f'Order ID: {order["order_id"]}, User ID: {order["user_id"]}, Item ID: {order["item_id"]}, Quantity: {order["quantity"]}')
    except KeyboardInterrupt:
        print('Consumer is shutting down...')
    finally:
        consumer.close()