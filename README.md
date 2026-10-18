This code is generate base on this tutorial:
https://youtu.be/xh_UWo5SuEI

to create the proyect: uv init --no-package
uv add confluent-kafka

To run docker-compose.yml: docker compose up -d (docker compose down -v, to down the container and it has been produced)

to create a topic: 
 docker compose exec kafka  /opt/kafka/bin/kafka-topics.sh --create --topic orders --partitions 3 --bootstrap-server localhost:9092

to run producer: uv run producer.py