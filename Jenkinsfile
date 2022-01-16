pipeline {
  agent any

  tools {
    maven 'maven'
  }

  environment {
    VERSION = readMavenPom().getVersion()
  }

  stages {
    stage('Build') {
      steps {
        sh 'mvn clean package'
      }
    }

    stage('Test') {
      steps {
        echo 'No test as of now.'
      }
    }

    stage('Deploy') {
      steps {
        nexusArtifactUploader artifacts: [[artifactId: 'py-gitops-app', classifier: '', file: "target/py-gitops-app-${VERSION}.zip", type: 'zip']], credentialsId: 'nexus', groupId: 'com.sanmuk', nexusUrl: "${env.NEXUS_URL}", nexusVersion: 'nexus3', protocol: 'http', repository: 'snapshot', version: "${VERSION}"
      }
    }

    stage('Image Unix') {
      steps {
        script {
          dockerImageU = docker.build 'sanmuk21/py-gitops-app' + ":$VERSION" "Dockerfile-Unix"
        }
      }
    }

    stage('Push Unix'){
      steps {
        script {
          docker.withRegistry( 'https://registry-1.docker.io', 'dockerhub' ) {
            dockerImageU.push()
          }
        }
      }
    }

    stage('Image Windows') {
      steps {
        script {
          dockerImageW = docker.build 'sanmuk21/py-gitops-app-win' + ":$VERSION" "Dockerfile-Windows"
        }
      }
    }

    stage('Push Windows'){
      steps {
        script {
          docker.withRegistry( 'https://registry-1.docker.io', 'dockerhub' ) {
            dockerImageW.push()
          }
        }
      }
    }

  }
}
