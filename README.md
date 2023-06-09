# Fitness Tracker API
Fitness Tracker 

## Technology Stack
- [Python](https://www.python.org/ "python")
- [Postgres](https://www.postgresql.org/ "Postgres")
- [Django](https://www.django-rest-framework.org/ "Django")

## Formatter or Linters
- [Flake8](https://flake8.pycqa.org/en/latest/index.html# "Flake8")
- [Black](https://black.readthedocs.io/en/stable/ "Black") 
- [Isort](https://pycqa.github.io/isort/ "Isort")


## How to set up locally using Docker container - **Recommended**
### Prerequisite
- Make sure **Docker** is installed locally. *Checkout installation here* [Docker](https://www.docker.com/ "Docker")
- Make sure **Mysql** is installed locally. *Checkout installation here* [Mysql](https://www.mysql.com/ "Mysql")

1. Clone the project.
```sh
 git clone 
```
```sh
 cd
```
2. Change the env.example file to .env .
3. Run 
```sh
 docker-compose build --no-cache
```
4. Run 
```sh
 docker-compose build up
```

## Running Linters
```sh
 cd scripts
```
```sh
 ./run-linters.sh
```

## Generate Seeder
- Exercise
```sh
 ./manage seed_exercises
```
- Nutritions
```sh
 ./manage seed_nutritions
```

## Generate documentation
```sh
 ./manage.py spectacular --color --file schema.yml
```