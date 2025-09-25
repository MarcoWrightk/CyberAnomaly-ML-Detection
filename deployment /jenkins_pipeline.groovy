pipeline {
  stages {
    stage('Test') {
      steps {
        sh 'pytest tests/'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t anomaly-detector .'
      }
    }
    stage('Deploy') {
      steps {
        sh './deploy.sh'
      }
    }
  }
}

