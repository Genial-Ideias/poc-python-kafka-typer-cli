from typer import Typer, echo
from config import init_consumer, init_producer

app: Typer = Typer()

TOPIC_NAME = '<your topic>'
SERVER_ADDRESS = '<Your broker url>:<your broker port>'

@app.command()
def produce(message: str):
    echo(f"Produce message at topic {TOPIC_NAME}")
    producer = init_producer(SERVER_ADDRESS)
    producer.send(TOPIC_NAME, { "message": message })
    echo(f"Message sent")

@app.command()
def consume(groupid: str = None, mode: str = 'latest'):
    echo(f"Consume message at group {groupid} at topic {TOPIC_NAME}")
    consumer = init_consumer(SERVER_ADDRESS, groupid, mode)
    consumer.subscribe([TOPIC_NAME])
    for msg in consumer:
        echo(msg.value)

if __name__ == '__main__':
    app()