pipeline {

    agent any



    stages {

        stage('Checkout') {

            steps {

                checkout scm

            }

        }



        stage('Build') {

            steps {

                sh '''

                    python3 -m venv .venv

                    .venv/bin/python -m pip install --upgrade pip

                    .venv/bin/python -m pip install -r requirements.txt

                '''

            }

        }



        stage('Test') {

            steps {

                sh '''

                    .venv/bin/python -m pytest -v \

                        --junitxml=test-results.xml

                '''

            }

        }



        stage('Package') {

            steps {

                sh '''

                    mkdir -p dist

                    tar -czf "dist/calculator-${BUILD_NUMBER}.tar.gz" \

                        calculator.py \

                        requirements.txt

                '''

            }

        }



        stage('Deploy') {

            steps {

                sh '''

                    mkdir -p deployed

                    cp "dist/calculator-${BUILD_NUMBER}.tar.gz" deployed/

                '''

            }

        }

    }



    post {

        always {

            junit 'test-results.xml'

            archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true

        }



        success {

            echo 'Pipeline completed successfully.'

        }



        failure {

            echo 'Pipeline failed. Check the console output.'

        }

    }

}
