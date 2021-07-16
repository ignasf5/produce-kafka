from confluent_kafka import Producer
import pandas as pd
import json

conf = {'bootstrap.servers': "192.168.0.42:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)

header_list = ["userid", "game", "behavior", "hours", "nx"]
df = pd.read_csv('steam-200k.csv', names=header_list)

#json = df.to_json()

#json_split = df.to_json(orient ='split')
#print("json_split = ", json_split, "\n")

#json_records = df.to_json(orient ='index')
for i in df.index: 
    test = df.loc[i].to_json()
    print(test) 
    producer.produce("steam", key="key", value=test)

#print("json_records = ", json_records, "\n")

#("row{}.json".format(i))

#json_records = [{“col1″:”1”, “col2″:”2”}, {“col1″:”3”, “col2″:”4”}]

#p = Producer({'bootstrap.servers': 'localhost:9092'})
#p.produce('steam', json.dumps({"demo": "message"}))