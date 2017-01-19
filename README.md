# wstest
Django and DRF test project


## To start development:
1. install [docker](https://docs.docker.com/#/components) and [docker-compose](https://docs.docker.com/compose/install/)
2. run `docker-compose web build` to build web container
4. run `docker-compose run web python manage.py migrate`
5. run `docker-compose run web python manage.py createsuperuser`

## To run project:
1. run `docker-compose web up`
2. point Your browser to `localhost:8000`
3. press `CTRL+C` to stop

## To run uni tests
1. run `docker-compose up tests`