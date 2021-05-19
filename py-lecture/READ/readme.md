# REcognize Alphabet Digits (READ)

There are three parts in this project:
- Image preprocess
- Image detection model
- Web-based human interface

# Getting Start
This project uses `pipenv` to manage the python version and python packages, and which has a dependency on `pyenv`, if you are not yet to install them, you should install them first.

## Environment
Run the following command at the **root path** of this project to install all packages.
```
$ pipenv install 
```

And run the following command to enter in the virtual environment:
```
$ pipenv shell 
```

## Run the server
The server is based on `Flask`, to run the server, just type:
```
python serv.js
```

then, the server would start listening on the port `10418`.
