#!/bin/bash

echo "======================="
echo "start activaction venv"
echo "======================="

source venv/bin/activate

echo "======================="
echo "venv in esecuzione"
echo "======================="

cd todolist

echo "======================="
echo "ti trovi in:"
pwd
echo "======================="

python manage.py makemigrations

echo "======================="
echo "migrazioni create, inizio a migrare"
pwd
echo "======================="

python manage.py migrate