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
       stage('cleanup stage') {
            steps {
                sh 'docker rmi myimage'
                sh 'docker rm -f $(docker ps -aq)'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myimage .'
            }
        }
       stage('Build and Push Image') {
            steps {
                
                try {
                    sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    sh 'docker push abhinavrout9490/myimage'
                } catch (err) {
                    echo "Error pushing image: ${err}"
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