pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'python calculator.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test commands here if any
            }
        }
    }
    post {
        success {
            echo 'Build Successful'
        }
        failure {
            echo 'Build Failed'
        }
    }
}