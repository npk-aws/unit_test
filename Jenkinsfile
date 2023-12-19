pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/npk-aws/unit_test.git'
            }
        }
        stage('Run Unit Test') {
            steps {
                // Add your unit test execution steps here
            }
        }
    }
}
