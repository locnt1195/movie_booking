pipeline {
  agent { docker { image 'python:3.6' } }
  stages {
    stage('build') {
      steps {
        sh 'python -m pip install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'pyttest test_app.py'
      }   
    }
  }
}
