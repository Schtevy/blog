# schtevy.de


# Local Development

```zsh
source .venv/bin/activate
pip install -r requirements.txt
```

Create your own `.env` file in the root folder of this project
```
DJANGO_SECRET_KEY='a-random-generated-string'
DATABASE_USER_PASSWORD='example'
DATABASE_HOST='127.0.0.1'
DATABASE_PORT='5432'
DATABASE_NAME='schtevy'
DATABASE_USER='django'
DJANGO_DEBUG_MODE=True
```

Add the env variables to your shell
```zsh
set -o allexport; source .env; set +o allexport
```

Check if the env variables are set correctly
```zsh
printenv | grep 'DJANGO\|DATABASE'
```

Run the docker stack with the test database
```zsh
docker stack deploy -c schtevy/stack.yml postgres
```

```zsh
python schtevy/manage.py makemigrations about
python schtevy/manage.py makemigrations blog
python schtevy/manage.py makemigrations opendata
python schtevy/manage.py migrate
```

Run the web server
```zsh
python schtevy/manage.py runserver
```

----

Naming convention for new branches.

```zsh
^[\d]{1,3}-[a-z0-9\-]{7,20}[a-z0-9]$
```

