pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
    }
    stages {
        // Stage 1
        stage('Cloning the repository from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/awaistahseen009/testing-jenkins'
            }
        }
        // Stage 2
        stage('Setting up the virtual env and installing dependencies') {
            steps {
                echo "Installing the dependencies"
                sh '''
                python3 -m venv ${VENV_DIR}
                . ./${VENV_DIR}/bin/activate
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }
        // Stage 3
        stage('Running code analysis with SonarQube') {
            environment {
                scannerHome = tool 'sonarqube'
            }
            steps {
                withSonarQubeEnv(credentialsId: 'sonarqube-token', installationName: 'sonarserver') {
                    sh '''
                    . ./${VENV_DIR}/bin/activate
                    ${scannerHome}/bin/sonar-scanner \
                      -Dsonar.projectKey=pythonProject \
                      -Dsonar.projectName=pythonProject \
                      -Dsonar.projectVersion=1.0 \
                      -Dsonar.sources=. \
                      -Dsonar.python.version=3 \
                      -Dsonar.exclusions=venv/**,requirements.txt
                    '''
                }
            }
        }
    }
   
}