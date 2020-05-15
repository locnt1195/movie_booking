pipeline {
  agent { docker { image 'python:3.6' } }
  stages {
    stage('build') {
      steps {
        sh 'python3 -m venv env'
        sh 'source ./env/bin/activate'
        sh 'python -m pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'source ./env/bin/activate'
        sh 'pyttest test_app.py'
      }   
    }
  }
}
