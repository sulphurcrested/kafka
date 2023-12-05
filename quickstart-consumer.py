## created by Samih Hijwel - 4 Dec 2023

from kafka import KafkaConsumer
import time, sys
import argparse


def main():
    # consumer arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--server", default="localhost", \
                           help="bootstrap server address")
    argParser.add_argument("-p", "--port", default=9092, type=int, \
                           help="bootstrap server port")
    argParser.add_argument("-t", "--topic", default="quickstart-events", \
                           help="kafka topic")

    args = argParser.parse_args(sys.argv[1:])

    print(f"quickstart-consumer broker:{args.server} and port:{args.port}")
    print(f"quickstart-consumer will start using topic:{args.topic}")
    # wait 30 seconds to allow kafka to initialise
    time.sleep(30)

    consumer = KafkaConsumer(bootstrap_servers=[f"{args.server}:{args.port}"], auto_offset_reset='earliest')
    consumer.subscribe([args.topic])

    for event in consumer:
        # print(type(event))
        # print(event)
        print(event.value.decode())


if __name__ == "__main__":
    main()