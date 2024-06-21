pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        DOCKER_IMAGE = "chand93/flask-app:${env.BUILD_NUMBER}"
        DOCKER_REGISTRY = "docker.io"  // Replace with your Docker registry URL
    }

    stages {
        stage('Build') {
            steps {
                script {
                    def dockerImage = docker.build("${DOCKER_REGISTRY}/${DOCKER_IMAGE}", "-f Dockerfile .")
                    dockerImage.inside {
                        sh 'echo "Build environment: $BUILD_NUMBER"'
                    }
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    docker.withRegistry("${DOCKER_REGISTRY}", 'dockerhub-credentials-id') {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Successfully built and pushed Docker image ${DOCKER_IMAGE}"
        }
        failure {
            echo "Failed to build or push Docker image"
        }
    }
}
