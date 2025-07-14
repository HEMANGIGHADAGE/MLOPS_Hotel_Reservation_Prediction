pipeline{
    agent any

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
    }
}