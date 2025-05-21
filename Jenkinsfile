pipeline {
    agent any
    
    environment {
        VENV_DIR = "venv"
    }
    
    stages {
        stage('Cloning the repository from the github') {
            steps {
                git branch: 'main', url: 'https://github.com/awaistahseen009/testing-jenkins'
            }
        }
        
        stage("Setting up the virtual env and installing the dependencies") {
            steps {
                echo "Installing the dependencies"
                sh '''
                python -m venv ${VENV_DIR}
                chmod 700 ./${VENV_DIR}/bin/activate
                . ./${VENV_DIR}/bin/activate
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }
        
        stage("Running the code analysis using SonarQube") {
            environment {
                scannerHome = tool "sonarqube"
            }
            steps {
                withSonarQubeEnv("sonarserver") {
                    sh '''
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

        stage("Quality Gate"){
            steps {
                timeout(time:1, units: 'HOURS'){
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}