from kafka import KafkaProducer
import json, random, time
from datetime import datetime as dt
import argparse, sys


def main():
    # producer arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--server", default="localhost", \
                           help="bootstrap server address")
    argParser.add_argument("-p", "--port", default=9092, type=int, \
                           help="bootstrap server port")
    argParser.add_argument("-t", "--topic", default="quickstart-events", \
                           help="kafka topic")
    argParser.add_argument('-T', "--tick", default=10, type=int, \
                           help="time between messages in seconds")

    args = argParser.parse_args(sys.argv[1:])

    print(f"quickstart-producer broker:{args.server} and port:{args.port}")
    print(f"a message will be produced on topic:{args.topic} every {args.tick} seconds")
    # wait 30 seconds to allow kafka to initialise
    time.sleep(30)

    producer = KafkaProducer(bootstrap_servers=[f"{args.server}:{args.port}"])
    count = 1
    while True:
        message = random_message(count)
        #message = "Test "+str(count)
        print(message)
        producer.send(args.topic, json.dumps(message).encode('utf-8'))
        #producer.send(topic, message.encode())
        count += 1
        time.sleep(args.tick)
        if count > (2**32):
            print(f"message serial number {count} has been reset to 1")
            count = 1
            # break


def random_message(count=1):
    return {
        'serial' : count,
        'text'   : "This is my message number "+str(count),
        'value' : random.randrange(99999999999),
        'timestamp' : dt.timestamp(dt.now())
    }




if __name__ == "__main__":
    main()