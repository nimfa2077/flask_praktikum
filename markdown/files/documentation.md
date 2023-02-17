# Process of installing and setting up a server with Python, WSGI and SLL key

### 0. Server Kaufen

### 1. Installier Python und Pip

    apt-get update
    apt-get upgrade
    apt-get intall python3
    apt-get install python3-pip

### 2. Mit Pip installier virtual environment package

    pip install virtualenv

### 3. Create and activate virtual environment

    virtualenv py-env
    source py-env/bin/activate

### 4. Install all required packages

    pip install flask gunicorn markdwon pdfkit

### 5. Install Git and download your project




(source)[https://www.odoo.com/de_DE/forum/hilfe-1/how-to-install-pip-in-python-3-on-ubuntu-18-04-167715]
