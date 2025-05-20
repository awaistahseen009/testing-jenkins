pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
    }
    stages {
        stage('Cloning the repository from the github') {
            git branch: 'main', url: 'https://github.com/awaistahseen009/testing-jenkins'
        }
        stage("Setting up the virtual env and installing the dependencies"){
            steps {
                echo "Installing the dependencies"
                sh '''
                python -m venv ${VENV_DIR}
                ./${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
    }
}