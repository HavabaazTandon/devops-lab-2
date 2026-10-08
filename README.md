# DevOps Lab 2 - Containerization & Kubernetes Orchestration

**Student:** Aaryan Tandon  
**Enrollment No.:** 2301730314  
**Course:** B.Tech CSE (AIML)  
**Section:** E  

## Objective

To containerize a Flask application using Docker and deploy it using Kubernetes (Minikube). The lab also demonstrates Docker storage, networking, Docker Compose, Kubernetes scaling, rolling updates, rollback, and continuous deployment using Jenkins.

## Technologies Used

- Python / Flask
- Docker
- Docker Compose
- Docker Hub
- Kubernetes
- Minikube
- Jenkins
- Git & GitHub
- Ubuntu 24.04 LTS (WSL)

## Project Structure

```text
devops-lab-2/
├── app/
│   ├── app.py
│   └── requirements.txt
├── bind-data/
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── compose.yaml
├── Jenkinsfile
├── .gitignore
└── README.md
```

## Tasks Completed

1. Kubernetes Deployment and Service
2. Kubernetes scaling, rolling update and rollback
3. Containerization and orchestration
4. Docker containerization
5. Docker container/image management and Docker Compose
6. Docker storage using container layer, named volume and bind mount
7. Docker container networking
8. Jenkins and Kubernetes continuous deployment
9. Documentation of commands, manifests, screenshots and observations

## Important Commands

### Docker

```bash
docker build -t devops-lab2-app:v1 .
docker run -d --name lab2-app -p 5000:5000 devops-lab2-app:v1
docker compose up -d
```

### Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get all
```

### Scaling

```bash
kubectl scale deployment lab2-app-deployment --replicas=4
```

### Rolling Update

```bash
kubectl set image deployment/lab2-app-deployment lab2-app=aaryantandon/devops-lab2-app:v2
kubectl rollout status deployment/lab2-app-deployment
```

### Rollback

```bash
kubectl rollout undo deployment/lab2-app-deployment
```

## CI/CD Pipeline

Jenkins was integrated with Kubernetes to automate deployment.

The pipeline performs:

1. Kubernetes connectivity verification
2. Application deployment using Kubernetes manifests
3. Deployment and rollout verification

The pipeline configuration is stored in the `Jenkinsfile`.

## Result

The Flask application was successfully containerized using Docker and deployed on Kubernetes using Minikube.

Docker storage, networking and Docker Compose were demonstrated successfully. Kubernetes scaling, rolling updates, rollback, and Jenkins-based continuous deployment were also implemented and verified.
