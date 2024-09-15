pipeline {
    agent any

    environment {
        BROWSERSTACK_USERNAME = 'xp_wQRfve'
        BROWSERSTACK_ACCESS_KEY = 'Jxn4E9RzqwXjNVLyxkok'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/XP2600-hub/nhorizonapp-blue.git'
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 test_index.py' 
                }
            }
        }
    }

    post {
        always {
            echo "done!"
        }
    }
}
