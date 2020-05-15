pipeline {
  agent { docker { image 'python:3.6' } }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'pyttest test_app.py'
      }   
    }
  }
}
