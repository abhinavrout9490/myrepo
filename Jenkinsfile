pipeline {
    agent any
    environment {
       DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }
    stages {
        stage('Checkout code') {
            steps {
                git url: 'https://github.com/abhinavrout9490/myrepo.git', branch: 'main'
            }
        }
    //    stage('cleanup stage') {
    //         steps {
    //             sh 'docker rmi -f myimage'
    //             sh 'docker rm -f $(docker ps -aq)'
    //         }
    //     }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myimage .'
            }
        }
       stage('Build and Push Image') {
            steps {
                 withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker tag myimage abhinavrout9490/myimage'
                    sh 'docker push abhinavrout9490/myimage'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}