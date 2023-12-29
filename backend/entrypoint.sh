#!/bin/bash

echo "Testing connection to database..."

function db_ready(){
python <<END
import sys
import psycopg2

try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        host='db',
        password='postgres',
        port=5432,
        connect_timeout=3
    )
except:
    sys.exit(-1)
sys.exit(0)
END
}

until db_ready
do
    echo "Server is not yet ready..."
    sleep 2
done

echo "Server is up."

exec "$@"
