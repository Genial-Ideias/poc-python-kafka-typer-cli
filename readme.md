# How to use/configure (Python 3.8)

Install dependencies whith pip 
    pip install -r requirements.txt

Change configuration variables at main.py
    TOPIC_NAME=<topic name>
    SERVER_ADDRESS=<Kafka broker url>:<kafka broker port>

# Produce messages:
    pythom main.py produce {mesasge}
    // use with --help for more options

# Consume messages:
    pythom main.py consume 
    // use with --help for more options





    


