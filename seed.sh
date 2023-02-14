#!/bin/bash
rm -rf medbayapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations medbayapi
python manage.py migrate medbayapi
python manage.py loaddata users
python manage.py loaddata physicians
python manage.py loaddata records

# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands
