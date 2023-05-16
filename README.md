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

## Documentation API
http://127.0.0.1:8000/api/schema/docs

## Generate Secret Key
```sh
 ./scripts/run-secretkey.sh 
```

## Run kubernetes Manifest files
### Make sure on of the following is installed
 - **Minikube** is installed. *Checkout installation here* [Minikube](https://minikube.sigs.k8s.io/docs/ "Minikube")
 - **Kind** is installed. *Checkout installation here* [Kind](https://kind.sigs.k8s.io/ "Kind")

```sh
$ kubectl apply -f ops/
```

## Serve the application
```sh
$ kubectl port-forward service/fitnesstracker 8000:8000
```
## Get Node Address

```sh
$ kubectl get service fitnesstracker -o jsonpath='{.spec.clusterIP}'
```

```sh
$ kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}'
```