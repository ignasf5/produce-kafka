from confluent_kafka import Producer
import pandas as pd
import json

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': "test"}

producer = Producer(conf)

header_list = ["userid", "game", "behavior", "hours", "nx"]
df = pd.read_csv('steam-200k.csv', names=header_list)

for i in df.index: 
    test = df.loc[i].to_json()
    print(test) 
    producer.produce("steam", key="key", value=test)
    producer.poll(0)

