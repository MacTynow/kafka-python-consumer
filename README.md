# Kafka-consumer

Simple consumer using Pykafka https://github.com/Parsely/pykafka.

## Usage

```bash
pip install -r requirements.txt

kafka-consumer.py [-h] [-b BROKERS] -t TOPIC [-f] [--cafile CAFILE]
                         [--certfile CERTFILE] [--keyfile KEYFILE]

required arguments:
  -b BROKERS           url:port for a kafka broker (default localhost:9092)
  -t TOPIC             The topic to consume from

optional arguments:
  -h, --help           show this help message and exit
  -f, --follow         Consume from the latest offset
  --cafile CAFILE      The ca file if using a SSL context
  --certfile CERTFILE  The cert file if using a SSL context
  --keyfile KEYFILE    The private key file if using a SSL context
```
