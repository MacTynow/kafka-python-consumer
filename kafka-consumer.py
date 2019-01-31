import sys
import signal
import os
import argparse
from pykafka.common import OffsetType
from pykafka import KafkaClient, SslConfig
from distutils.util import strtobool


def signal_handler(signal, frame):
    print('Consumed %s messages', message_count)
    sys.exit(0)


parser = argparse.ArgumentParser(description='Simple kafka consumer')

parser.add_argument('-b', dest='brokers', default='localhost:9092', help='url:port for a kafka broker')
parser.add_argument('-t', dest='topic', required=True, help='The topic to consume from')
parser.add_argument('-f', '--follow', action="store_true", default=False, help='Consume from the latest offset')
parser.add_argument('--cafile', dest='cafile', help='The ca file if using a SSL context')
parser.add_argument('--certfile', dest='certfile', help='The cert file if using a SSL context')
parser.add_argument('--keyfile', dest='keyfile', help='The private key file if using a SSL context')

args = parser.parse_args()

brokers = args.brokers
topic = args.topic
is_using_latest_offset = args.follow
cafile = args.cafile
certfile = args.certfile
keyfile = args.keyfile
message_count = 0

if cafile is not None and certfile is not None and keyfile is not None:
  config = SslConfig(cafile=cafile,
                    certfile=certfile, 
                    keyfile=keyfile)
  client = KafkaClient(hosts=brokers, ssl_config=config)
else:
  client = KafkaClient(hosts=brokers)

topic = client.topics[str.encode(topic)]

signal.signal(signal.SIGINT, signal_handler)

auto_offset_reset = OffsetType.LATEST if is_using_latest_offset else OffsetType.EARLIEST
consumer = topic.get_simple_consumer(
    auto_offset_reset=auto_offset_reset
)
for message in consumer:
  if message is not None:
    print(message.offset, message.value)
    message_count += 1
