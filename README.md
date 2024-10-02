# Fitness Tracker API
The Fitness Tracker API project is designed to track exercises, nutrition, and workouts, utilizing a Python backend with Django and Postgres for the database.

## Technology Stack
- [Python](https://www.python.org/ "python")
- [Postgres](https://www.postgresql.org/ "Postgres")
- [Django](https://www.django-rest-framework.org/ "Django")

## Formatter or Linters
- [Flake8](https://flake8.pycqa.org/en/latest/index.html# "Flake8")
- [Black](https://black.readthedocs.io/en/stable/ "Black") 
- [Isort](https://pycqa.github.io/isort/ "Isort")

## How to set up locally 
### Prerequisite
- Make sure **Postgres** is installed locally. *Checkout installation here* [Postgres](https://www.postgresql.org/ "Postgres")

1. Clone the project.
```sh
 git clone https://github.com/CyrilBaah/fitnesstracker.git
```
```sh
 cd fitnesstracker
```
2. Create a virtual environment and activate it
```sh
 virtualenv env
 source env/bin/activate  
```
3. Install packages
```sh
 pip install -r requirements.txt 
```
4. Change the env.example file to .env and update it accordingly
5. Run migrations
```sh
python manage.py migrate
```
5. Start server
```sh
python manage.py runserver
```
5. Access the [fitnesstracker API](http://127.0.0.1:8000/api/schema/docs "Fitnesstracker API")

## How to set up locally using Docker container 
### Prerequisite
- Make sure **Docker** is installed locally. *Checkout installation here* [Docker](https://www.docker.com/ "Docker")
- Make sure **Postgres** is installed locally. *Checkout installation here* [Postgres](https://www.postgresql.org/ "Postgres")

1. Clone the project.
```sh
 git clone https://github.com/CyrilBaah/fitnesstracker.git
```
```sh
 cd fitnesstracker
```
2. Change the env.example file to .env 
3. Run 
```sh
 docker-compose build --no-cache
```
4. Run 
```sh
 docker-compose up
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
- Workout
```sh
 ./manage seed_workouts
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

## Serve minikube server | Dashboard
```sh
$ minikube dashboard --url
```
## Get Node Address

```sh
$ kubectl get service fitnesstracker -o jsonpath='{.spec.clusterIP}'
```

```sh
$ kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}'
```

## Configure Ingress
Get ClusterIP
```sh
$ kubectl get service fitnesstracker
```
Modify /etc/hosts
```sh
$ sudo nano /etc/hosts
```
Add cluster IP to /etc/hosts
```bash
123.456.7.8 fitnesstracker.com
```

## Use [KinD](https://kind.sigs.k8s.io/ "KinD")
1. Run
```
make create-cluster
```
2. Install Nginx Ingress Controller
```
make install-nginxingresscontroller 
```