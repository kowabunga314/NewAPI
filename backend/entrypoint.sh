#!/bin/bash

echo "Testing connection to database..."

while [ $(pg_isready --host=db -q) ]
do
    echo "Server is not yet available, waiting..."
    sleep 2
done

echo "Server is up."

exec "$@"
