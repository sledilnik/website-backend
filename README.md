# Website backend

A collection of backend administrative modules for various parts of the website.

## Development setup

This is a python and [Django](https://www.djangoproject.com/) based project.

It includes the setup for the [pipenv](https://docs.pipenv.org/) python virtual environment and package management. Please install it first and then run:

```shell
pipenv install --dev
pipenv shell
```

You can leave the created virtual environment by running `exit` from the shell.

Second, you need to link the development settings file and create a secrets file:

```shell
cd sledilnik/settings
ln -s develop.py __init__.py
cat "SECRET_KEY = 'secret-key'" > secrets.py
cd -
```

Finally, crete the databse and run migrations:

```shell
./manage migrate
```

Create a superuser by:

```shell
./manage.py createsuperuser
```

Finally, run the server and visit the admin section at http://127.0.0.1:8000/admin/:

```shell
./manage.py runserver
```

## Deployment

Helm chart used is `sledilnik/django` located in https://github.com/sledilnik/helm-repo/

### Manual deploy (for development)

Change `../helm-repo/charts/django` with path to local checkout of helm chart, do modifications and try it out.

```
helm upgrade website-backend-stage ../helm-repo/charts/django --install --atomic --namespace sledilnik-stage  -f .helm/values.stage.yml --debug
```