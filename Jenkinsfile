/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Testing Github localy') {
            steps {
                dir('C:\Users\Alili\OneDrive\Skrivbord\Gym_Tester'){
                    bat 'python -m pytest'
            }
        }
    }
        stage('Clean Workspace'){
           steps {
               cleanWs()
    }
        }
    }
}
