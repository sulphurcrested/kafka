FROM python:3.9.18-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# default is producer
# ARG APP="quickstart-producer.py"
COPY ${APP} ./
RUN echo "starting "${APP}
CMD env;if [ "X"${APP_TICK} != "X" ]; then \
        python /usr/src/app/${APP} --server ${KAFKA_SERVER} --port ${KAFKA_PORT} --topic ${KAFKA_TOPIC} --tick ${APP_TICK}; \
    elif [ "X"${KAFKA_TOPIC_LISTEN} != "X" ]; then \
        python /usr/src/app/${APP} --server ${KAFKA_SERVER} --port ${KAFKA_PORT} --listen ${KAFKA_TOPIC_LISTEN} --echo ${KAFKA_TOPIC_ECHO}; \
    else \
        python /usr/src/app/${APP} --server ${KAFKA_SERVER} --port ${KAFKA_PORT} --topic ${KAFKA_TOPIC}; \
    fi;