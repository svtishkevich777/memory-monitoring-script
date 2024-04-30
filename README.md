# memory-monitoring-script
# setup

clone the repository
```sh
$ git clone git@github.com:svtishkevich777/memory-monitoring-script.git
$ cd memory-monitoring-script
```
Create a virtual environment to install dependencies in and activate it:
```sh
1. First update the PIP
$ python3 -m pip install --upgrade pip
```
```sh
2. Next we indicate the python version with which we want to work
   and the name of the virtual environment.
$ virtualenv -p python3.8 .venv
```
```sh
3. And then activate the created virtual environment
$ source .venv/bin/activate
```
```sh
4. Then you need to set the dependencies:
(.venv)$ pip install -r requirements.txt
```
```sh
5. Now you can run the script in the terminal..
$ python main.py
```
```sh
6. To run tests in the terminal
$ python test_memory.py
```

# Description of the task
```sh
Написать bash или python или groovy скрипт,
который будет контролировать потребление памяти и
генерировать alarm путем отправки http запроса на API.
```