pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'echo Build step on Windows'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing the project...'
                bat 'python calculator.py'
            }
        }
    }
}