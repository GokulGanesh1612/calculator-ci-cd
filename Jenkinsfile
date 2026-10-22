pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Creating Python virtual environment'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating application package'

                powershell '''
                    New-Item -ItemType Directory -Force -Path dist | Out-Null

                    $packageName = "dist/calculator-$env:BUILD_NUMBER.zip"

                    Compress-Archive `
                        -Path calculator.py, requirements.txt `
                        -DestinationPath $packageName `
                        -Force

                    Write-Host "Created package: $packageName"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application package'

                powershell '''
                    New-Item -ItemType Directory -Force -Path deployed | Out-Null

                    $packageName = "dist/calculator-$env:BUILD_NUMBER.zip"

                    Copy-Item `
                        -Path $packageName `
                        -Destination deployed `
                        -Force

                    Write-Host "Deployment completed."
                '''
            }
        }
    }

    post {
        always {
            echo 'Archiving test results and build artifacts'

            junit(
                testResults: 'test-results.xml',
                allowEmptyResults: true
            )

            archiveArtifacts(
                artifacts: 'dist/*.zip',
                fingerprint: true,
                allowEmptyArchive: true
            )
        }

        success {
            echo 'Build, tests, packaging, and deployment completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Review the console output for details.'
        }
    }
}
