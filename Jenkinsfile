pipeline {
    agent any
    environment {
        DOCKER_USERNAME = 'abhinavrout9490'
        DOCKER_PASSWORD = credentials('dockerhub-credentials') 
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
                    sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    sh 'docker tag myimage abhinavrout9490/myimage'
                    sh 'docker push abhinavrout9490/myimage'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}