# README

## `Requirements`

To run this project you will need following setup:

[Ubuntu 20.04 LTS](https://ubuntu.com/#download)</br>
[Python version 3.8.5](https://www.python.org/downloads/)</br>
[Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)</br>
[Selenium](https://pypi.org/project/selenium/)</br>

## `Installation`

### **_Python_**

To install python run following commands on your terminal.

1. $ sudo apt-get install software-properties-common</br>
2. $ sudo add-apt-repository ppa:deadsnakes/ppa</br>
3. $ sudo apt-get update</br>
4. $ sudo apt-get install python3.8</br>

### **_Flask_**

$ pip install flask</br>
OR</br>
$ pip3 install flask</br>

### **_Selenium_**
$ pip install selenium</br>
OR</br>
$ pip3 install selenium</br>

## `Run the project`

Before actually running the code execute the below commands in your project directory (Run these commands only for the first time).

1. $ export FLASK_APP=app.py (File name in which flask code and routes are setup)</br>
2. $ export FLASK_DEBUG=1  (This helps to see changes as soon as you save code instead of running the entire code again)</br>

After executing above commands you are ready to run the project.

$ python app.py</br>
OR</br>
$ python3 app.py

Open [https://localhost:5000](https://localhost:5000) to view it on browser.</br>
The list of errors will be displayed on terminal
