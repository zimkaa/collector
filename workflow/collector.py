import sys

from confluent_kafka import Consumer

import config


consumer = Consumer({
    'bootstrap.servers': f'{config.HOST}:9092',
    'group.id': 'listener_filtred_events',
    'auto.offset.reset': 'earliest',
})

consumer.subscribe(['filtred'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    sys.stdout.write(msg.value().decode("utf-8"))
    print(msg.value().decode("utf-8"))

consumer.close()


sys.stdout.write(str)
