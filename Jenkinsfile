pipeline {
  agent { docker { image 'python:3.6' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pyttest test_app.py'
      }   
    }
  }
}
