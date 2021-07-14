from kafka import KafkaProducer, KafkaConsumer
import json

def init_producer(server) -> KafkaProducer:
    producer = KafkaProducer(bootstrap_servers=server, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    return producer

def init_consumer(server, groupid, mode='latest') -> KafkaConsumer:
    consumer = KafkaConsumer(
                    bootstrap_servers=server, 
                    group_id=groupid,
                    auto_offset_reset=mode,
                    value_deserializer=lambda v: json.loads(v))
    return consumer