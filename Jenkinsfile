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
				// IF %errorlevel% NEQ 0 ( exit /b %errorlevel% ) 
				"""
            }
        }
        stage('Finalize') {
            steps {
                echo 'Finalize....'
				bat """
					set container_id = docker ps -q --filter name=game_server
					docker stop %container_id%
					docker rm %container_id%
				"""
            }
        }		
    }
}
