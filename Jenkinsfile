/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Testing Github localy') {
            steps {
                dir('C:/Users/Alili/OneDrive/Skrivbord/.Jenkins/workspace/Gym_Tester/Test_grossisten'){
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
