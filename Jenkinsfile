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

                bat '''
                    if exist venv rmdir /s /q venv

                    where py >nul 2>&1
                    if %ERRORLEVEL% EQU 0 (
                        py -3 -m venv venv
                    ) else (
                        python -m venv venv
                    )

                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python unit tests'

                bat '''
                    venv\\Scripts\\python.exe -m pytest -v --junitxml=test-results.xml
                '''
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
