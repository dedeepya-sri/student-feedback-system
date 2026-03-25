pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/student-feedback-system.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t student-feedback-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 5000:5000 student-feedback-app'
            }
        }
    }
}