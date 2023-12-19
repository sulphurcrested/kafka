## created by Samih Hijwel - 19 Dec 2023

from kafka import KafkaConsumer, KafkaProducer
import time, sys
import argparse


def main():
    # consumer arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--server", default="localhost", \
                           help="bootstrap server address")
    argParser.add_argument("-p", "--port", default=9092, type=int, \
                           help="bootstrap server port")
    argParser.add_argument("-l", "--listen", default="looper-listen", \
                           help="kafka listening topic")
    argParser.add_argument("-e", "--echo", default="looper-echo", \
                           help="kafka echo topic")

    print ("parsing looper arguments")
    args = argParser.parse_args(sys.argv[1:])

    print(f"looper broker:{args.server} and port:{args.port}")
    print(f"looper will start listening to topic:{args.listen} and echo to topic {args.echo}")
    # wait 30 seconds to allow kafka to initialise
    time.sleep(30)

    consumer = KafkaConsumer(bootstrap_servers=[f"{args.server}:{args.port}"], auto_offset_reset='earliest')
    consumer.subscribe([args.listen])
    producer = KafkaProducer(bootstrap_servers=[f"{args.server}:{args.port}"])

    for msg in consumer:
        print(f"looping: {msg.value.decode()}")
        producer.send(args.echo, msg.value)



if __name__ == "__main__":
    main()