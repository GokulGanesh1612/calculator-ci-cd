pipeline {
    agent {
        label 'windows'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                bat '''
                    py -3 --version
                    py -3 -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    .venv\\Scripts\\python.exe -m pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pytest ^
                        --junitxml=test-results.xml ^
                        -v
                '''
            }
        }
    }

    post {
        always {
            junit(
                testResults: 'test-results.xml',
                allowEmptyResults: true
            )

            archiveArtifacts(
                artifacts: 'test-results.xml',
                allowEmptyArchive: true
            )
        }

        success {
            echo 'All tests passed successfully.'
        }

        failure {
            echo 'The build or tests failed. Check the console output.'
        }
    }
}
