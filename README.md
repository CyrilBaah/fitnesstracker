# 
# 🏋️‍♂️ Fitness Tracker API 🏋️‍♀️

The Fitness Tracker API is designed to keep you on top of your fitness goals by tracking exercises, nutrition, and workouts! This robust API leverages Python with Django and Postgres for a smooth experience.


## 🌟 Technology Stack
Backend : [Python](https://www.python.org/)🐍

Database: [Postgres](https://www.postgresql.org/) 🐘

Framework:[Postgres](https://www.djangoproject.com/)🦄
## 🛠️ Code Formatters & Linters
Flake8: Enforcing code standards [Flake8](https://flake8.pycqa.org/en/latest/index.html#)⚙️

Black: Code formatting [Black](https://black.readthedocs.io/en/stable/) 🖤

Isort: Sorting imports [Isort](https://pycqa.github.io/isort/) 📑

## 🚀 How to Set Up Locally

Pre-requisite
Ensure Postgres is installed. Check the installation guide here.
Steps

1.Clone the Project:

```bash
git clone https://github.com/CyrilBaah/fitnesstracker.git
```
```bash
cd fitnesstracker
```
2.Set Up Virtual Environment:
```bash
virtualenv env
source env/bin/activate
```
3.Install Dependencies:
```bash
pip install -r requirements.txt
```
4.Update Environment Variables:
Rename the `env.example` file to `.env` and update it as needed.

5.Run Migrations:
```bash
python manage.py migrate
```
6.Start the Server:
```bash
python manage.py runserver
```
7.Access the API: Visit:  [Fitness Tracker API 🌐](http://127.0.0.1:8000/api/schema/docs) 


## 🐳 Docker Setup
Pre-requisite

Install Docker: [Installation Guide](https://www.docker.com/)

Install Postgres: [Installation Guide](https://www.postgresql.org/)

Steps:

1.Clone the repository
``` bash
git clone https://github.com/CyrilBaah/fitnesstracker.git
cd fitnesstracker
```
2.Update Environment Variables:
Rename the `env.example` file to `.env` and update it as needed.

3.Run 
```sh
docker-compose build --no-cache
```
4.Run 
```sh
docker-compose up
```
## 🛡️ Running Linters

```sh
 cd scripts
```
```sh
 ./run-linters.sh
```
## 📊 Generate Seeders

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
## 📜 Generate API Documentation
```sh
 ./manage.py spectacular --color --file schema.yml
```

## Documentation API
http://127.0.0.1:8000/api/schema/docs
## 🔐 Generate Secret Key
```sh
 ./scripts/run-secretkey.sh 
```
## 🏗️ Kubernetes Setup

Prerequisites

- Install **Minikube**.  [Minikube](https://minikube.sigs.k8s.io/docs/ "Minikube")
 - Install **Kind**.  [Kind](https://kind.sigs.k8s.io/ "Kind")

Steps:

1.Apply Kubernetes manifests:
```sh
$ kubectl apply -f ops/
```
2.Port-forward the service:
```sh
$ kubectl port-forward service/fitnesstracker 8000:8000
```
3.Access Minikube dashboard:
```sh
$ minikube dashboard --url
```
4.Get Node Address:
```sh
$ kubectl get service fitnesstracker -o jsonpath='{.spec.clusterIP}'
```
```sh
$ kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}'
```
5.Configure Ingress:

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



##🚀 Use [KinD](https://kind.sigs.k8s.io/ "KinD")

1. Run
```
make create-cluster
```
2. Install Nginx Ingress Controller
```
make install-nginxingresscontroller 
```
## 🤝 Contributing

We 💙 contributions! Here's how you can contribute to the project:

1.Steps to Contribute
Fork the Repository: Click on the "Fork" button on the repository page to create your own copy.

2.Clone Your Fork

Once you’ve forked the project, clone your copy to your local machine:
```bash
git clone https://github.com/YOUR-USERNAME/fitnesstracker.git
cd fitnesstracker
```
3.Create a New Branch:
```bash
git checkout -b feature-branch-name
```
4.Make Your Changes: Add features, fix bugs, or enhance documentation.

5.Commit Your Changes:

Write clear and descriptive commit messages. Your commit messages should be short and concise, summarizing the changes.
```bash
git commit -m "Add feature or fix description"
```
6.Push to Your Fork:
```bash
git push origin feature-branch-name
```
7.Submit a Pull Request: Open a pull request from your fork to the original repository with a clear description.

We look forward to your awesome contributions! 🎉