pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
				echo 'Checkout..'
				cleanWs()
				checkout scm

            }
        }
        stage('Build') {
            steps {
                echo 'Build..'
				bat """
				docker-compose up --build -d
				"""
            }
        }
        stage('Test') {
            steps {
                echo 'Test....'
				bat """
				python tests\\e2e.py 
				echo %errorlevel%
				"""
            }
        }
        stage('Finalize') {
            steps {
                echo 'Finalize....'
				bat """
				docker-compose down
				"""
            }
        }		
    }
	
	post {
		failure {
			echo "failure"
			bat """
			docker-compose down
			"""
		}
	}
}
