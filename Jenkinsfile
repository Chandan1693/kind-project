pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id') // Ensure correct credential ID
        DOCKER_IMAGE = "chand93/flask-app:${env.BUILD_NUMBER}"
        DOCKER_REGISTRY = "docker.io"
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
                    docker.withRegistry("${DOCKER_REGISTRY}", 'dockerhub-credentials-id') {  // Ensure correct credential ID
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
