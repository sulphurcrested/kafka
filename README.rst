Custom Kafka server
====================

Dockerfile compose to build a custom kafka zookeeper and broker based on bitnami/kafka docker image

Please see ``https://hub.docker.com/r/bitnami/kafka?uuid=05A5F6EA-98AD-4401-B432-D8A3448FBF45`` for
more information.

Getting Started
---------------
1- Install Docker (or Docker Desktop) and make sure the docker daemon is running
   https://www.docker.com/products/docker-desktop/

2- Customise the configuration using the environment variables in the `docker-compose.yml`
   file. Refer to the bitnami image link above for more info.

3- Run the docker containers using:
   ``docker-compose -f docker-compose.yml up --build --detached``
   this will run `kafka` service (zookeeper and broker) in addition to `kafka_producer` and
   `kafka_consumer` as two python services communicating through kafka

4- To run kafka service only use:
   ``docker-compose -f docker-compose.yml up --build --detached kafka``

Connecting to Kafka:
--------------------
The docker-compose.yml environment is configured to allow connecting to Kafka
(running under docker environment) using two ways:
- From within Docker, use host: kafka & port: 19092
- From the local host (outside of docker), use host: localhost & port 9092

This should be useful to run kafka in docker while developing your application on
the local host.