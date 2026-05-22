// node {
//     def PYTHON = 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'

//     try {
//         stage('Checkout') {
//             checkout scm
//         }

//         stage('show python version') {
//             bat "${PYTHON} --version"
//         }

//         stage('run python program') {
//                 bat "${PYTHON} extract_data.py" 
//         } 

//     }
//      catch (err) {
//         echo "Pipeline failed: ${err}"
//     }
// }





// pipeline {
//     agent any
//     environment {
//         PYTHON = 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
        
//     }

//     stages {
//         stage('Checkout code') {
//             steps {
//                 checkout scm
//             }
//         }
        
//         stage('install dependencies') {
//             steps {
//                 bat "${env.PYTHON} -m pip install -r requirements.txt"
//             }
//         }


//         stage('show python version') {
//             steps {
//                 bat "${env.PYTHON} --version"
//             }
//         }

//         stage('run extract_data.py') {
//             steps {
//                 bat "${env.PYTHON} extract_data.py"
//             }
//         }
//     }
// }




// #jenkins credential (DB_PASSWORD)




pipeline {
    agent any
    environment {
        PYTHON = 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
        DB_PASSWORD = credential('DB_PASSWORD')
        
    }

    stages {
        stage('Checkout code') {
            steps {
                checkout scm
            }
        }
        stage('run extract_data.py') {
            steps {
                bat """
                set DB_PASSWORD = ${env.DB_PASSWORD} 
                ${env.PYTHON} extract_data.py
                """
            }
        }
    }
}
    