pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning github repo to Jenkins')
        {
            steps{
                script{
                    echo 'Cloning github repo to Jenkins..'
                    checkout scmGit(branches: [[name: '*/masters']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/HEMANGIGHADAGE/MLOPS_Hotel_Reservation_Prediction.git']])
                }
            }
        }

        stage('Setting virtual env and installing dependencies')
        {
            steps{
                script{
                    echo 'Setting virtual env and installing dependencies'
                    sh ''' 
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}