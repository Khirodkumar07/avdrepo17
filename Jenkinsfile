node {
    def PYTHON = 'C:\\Users\\ACER\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'

    try {
        stage('Checkout') {
            checkout scm
        }

        stage('show python version') {
            bat "${PYTHON} --version"
        }

        stage('run python program') {
                bat "${PYTHON} extract_data.py" 
        } 

    }
     catch (err) {
        echo "Pipeline failed: ${err}"
    }
}
