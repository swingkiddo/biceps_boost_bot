#!/bin/sh
db=repsol_db
bot=repsol_bot
file=docker-compose.yml

docker compose -f $file down
docker rmi $db $bot
docker compose -f $file build
docker compose -f $file up