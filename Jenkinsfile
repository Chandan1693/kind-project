pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        DOCKER_IMAGE = "chand93/flask-app:${env.BUILD_NUMBER}"
        DOCKER_REGISTRY = "https://docker.io"  // Ensure Docker registry URL is correct
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
                    docker.withRegistry("${DOCKER_REGISTRY}", 'docker-credentials-id') {
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
