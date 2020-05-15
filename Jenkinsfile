pipeline {
  agent { docker { image 'python:3.6' } }
  stages {
    stage('build') {
      steps {
        sh 'echo "Installing Requirements"'
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip install --user -r requirements.txt'
        }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'python -m pytest test_app.py'
        }
      }   
    }
  }
}
