pipeline {
    agent any

    stages {
        stage('Verify Kubernetes') {
            steps {
                sh 'kubectl get nodes'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl rollout status deployment/lab2-app-deployment'
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
}
