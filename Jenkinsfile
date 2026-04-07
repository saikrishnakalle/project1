pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Execute Python script for build or validation
                bat 'python calculator.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run Python unit tests (requires a "tests" folder with test files)
                bat 'python -m unittest discover tests'
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