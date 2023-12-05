FROM python:3.9.18-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# default is producer
ARG APP="quickstart-producer.py"
COPY ${APP} ./
RUN echo "starting "${APP}
CMD if [ ${APP_TICK} ]; then \
        python /usr/src/app/${APP} --server ${KAFKA_SERVER} --port ${KAFKA_PORT} --topic ${KAFKA_TOPIC} --tick ${APP_TICK}; \
    else \
        python /usr/src/app/${APP} --server ${KAFKA_SERVER} --port ${KAFKA_PORT} --topic ${KAFKA_TOPIC}; \
    fi;