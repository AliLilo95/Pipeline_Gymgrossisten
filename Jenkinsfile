/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Testing Github localy') {
            steps {
                dir('C:\Users\Alili\OneDrive\Skrivbord\Tester_Zalando'){
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
