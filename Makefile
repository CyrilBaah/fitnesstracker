# Define variables
CLUSTER_NAME := dev
IMAGE_NAME := fitnesstracker
CONTAINER_NAME := fitnesstracker
PORT := 8000

.PHONY: create-cluster get-cluster set-context delete-cluster install-nginxingresscontroller get-nginxingress get-logs cluster-info get-nodes get-pods expose-frontend build run stop remove remove-image ps ps-all images exec clean help

create-cluster:
	@echo "Creating Kind cluster..."
	kind create cluster --config config.yml --name $(CLUSTER_NAME)

get-cluster:
	@echo "Getting Kind clusters..."
	kind get clusters

set-context:
	@echo "Setting kubectl context to $(CLUSTER_NAME)..."
	kubectl config use-context kind-$(CLUSTER_NAME)

delete-cluster:
	@echo "Deleting Kind cluster..."
	kind delete cluster --name $(CLUSTER_NAME)

push-image:
	docker push cyrilbaah/fitnesstracker:latest

install-nginxingresscontroller:
	@echo "Install NGINX Ingress Controller..."
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml

get-nginxingress:
	@echo "Get nginxingress pods..."
	kubectl get pods -n ingress-nginx -owide

get-logs:
	@echo "Get pods for logs command..."
	@echo "$ kubectl logs -f <name-app-xxx>"

cluster-info:
	@echo "Get cluster information..."
	kubectl cluster-info --context kind-$(CLUSTER_NAME)

get-nodes:
	@echo "Get cluster nodes..."
	kubectl get nodes -owide

get-pods:
	@echo "Get cluster pods..."
	kubectl get pods -owide

expose-backend:
	@echo "Get port for backend..."
	kubectl port-forward svc/$(CONTAINER_NAME) -n default 8000:8000

build:
	docker build -t cyrilbaah/$(IMAGE_NAME) .

run:
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

remove:
	docker rm $(CONTAINER_NAME)

remove-image:
	docker rmi $(IMAGE_NAME)

ps:
	docker ps

ps-all:
	docker ps -a

images:
	docker images

exec:
	docker exec -it $(CONTAINER_NAME) bash

clean:
	docker stop $(shell docker ps -aq) || true
	docker rm $(shell docker ps -aq) || true
	docker rmi $(shell docker images -aq) || true

help:
	@echo "Available targets:"
	@echo "  create-cluster   - Create the Kind cluster"
	@echo "  get-cluster      - List available Kind clusters"
	@echo "  set-context      - Set kubectl context to the Kind cluster"
	@echo "  delete-cluster   - Delete the Kind cluster"
	@echo "  get-pods         - List all pods"
	@echo "  get-nodes        - List all nodes"
	@echo "  expose-backend   - Makes backend app accessible"
	@echo "  get-nginxingress - List all nginx ingress"
	@echo "  get-logs         - Get logs command"
	@echo "  build            - Build Docker image"
	@echo "  run              - Run Docker container in detached mode"
	@echo "  stop             - Stop Docker container"
	@echo "  remove           - Remove Docker container"
	@echo "  remove-image     - Remove Docker image"
	@echo "  ps               - View running containers"
	@echo "  ps-all           - View all containers (including stopped ones)"
	@echo "  images           - View Docker images"
	@echo "  exec             - Execute a command inside the running container"
	@echo "  clean            - Clean up (stop and remove) all containers and images"
	@echo "  help             - Display this help message"

.DEFAULT_GOAL := help
