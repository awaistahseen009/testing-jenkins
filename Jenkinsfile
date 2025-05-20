pipeline {
    agent any
    tools {
        // This ensures SonarQube scanner is available
        // Make sure this tool name matches Jenkins Global Tool config
        sonarScanner 'sonarqube'
    }
    environment {
        VENV_DIR = "venv"
    }
    stages {
        // stage 1

        stage('Cloning the repository from the github') {
            steps {
            git branch: 'main', url: 'https://github.com/awaistahseen009/testing-jenkins'

            }
        }
        // Stage 2
        stage("Setting up the virtual env and installing the dependencies"){
            steps {
                echo "Installing the dependencies"
                sh '''
                python -m venv ${VENV_DIR}
                chmod 700 ./${VENV_DIR}/bin/activate
                ./${VENV_DIR}/bin/activate
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }
        // Stage 3
        stage("Running the code analysis using SonarQube"){
            environment {
                scannerHome = tool "sonarqube"
            }
            steps{
                withSonarQubeEnv("sonarserver"){
                    sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=pythonProject \
                    -Dsonar.projectName=pythonProject \
                    -Dsonar.projectVersion=1.0
                    -Dsonar.sources=. \
                    -Dsonar.python.version=3'''
                }
            }
        }

    }
}