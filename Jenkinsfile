pipeline {

    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install pytest requests'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

    }
}