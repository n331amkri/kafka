import uuid
import json
from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092',  
}
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.value().decode("utf-8")}')

order = {
    'order_id': str(uuid.uuid4()),
    "user_id": "user_1",
    "item_id": "item_1",
    "quantity": 2
    }

#need to convert the order dict to a string + byte before sending
value = json.dumps(order).encode('utf-8')
#if topic order is not there kafka will create it and add it to that topic
producer.produce(topic='orders', value=value,
                 callback=delivery_report)
 # Ensure all messages are sent before exiting,
 #  if the program ends before the message is sent as rpducer buffers and sends message in batches, 
 # it will be lost.
producer.flush() 