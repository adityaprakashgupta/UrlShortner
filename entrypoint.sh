# Base file with the entrypoint it will take two flags -m and -s
# -m will give command to run the django migrations
# -s will give command to run the django server
# if both flags are not provided it will run the django server by default
# if both flags are provided it will run the migrations first and then the server
# if only -m flag is provided it will run the migrations only
# if only -s flag is provided it will run the server only
# there is no proper order for this flags to be provided

# Check for -m flag and run migrations if present
if [ "$1" = "-m" ] || [ "$2" = "-m" ]; then
    echo "Running the migrations"
    python manage.py migrate
fi

# Check for -s flag and run server if present
if [ "$1" = "-s" ] || [ "$2" = "-s" ]; then
    echo "Running the server"
    python manage.py runserver 0.0.0.0:8000
fi
