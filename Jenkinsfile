pipeline {

  agent none

  stages {

    stage("Build"){
        git url: 'https://github.com/JimmyMagu/Test_jenkins.git'

        steps {
            //sh step to compile our python program
            sh 'python -m py_compile char.py num.py'
            //save compiled results to a stash file
            stash(name: 'compiled_results', includes: '*.py*')
        }
     }
    }
  }
  