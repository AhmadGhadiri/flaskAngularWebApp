#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"


until psql postgresql://postgres:0NLIN3-ex4m@"${host}":5432/online-exam -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
