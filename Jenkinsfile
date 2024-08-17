pipeline {
    agent any
   
    stages {
        stage('Checkout code') {
            steps {
                git url: 'https://github.com/abhinavrout9490/myrepo.git', branch: 'main'
            }
        }
       
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myimage .'
            }
        }
       
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }

    }
}