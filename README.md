# CHALLENGE: Build Your Own Web Server

In this repo I'm taking a shot at coding challenge to [build a web server](https://codingchallenges.fyi/challenges/challenge-webserver/)

This web server accepts multiple concurrent tcp connections. It's configured to process HTTP requests and respond accordingly.

It is written in python.

# Getting Started

## Requirements

- installation of python (3.12.3^)

## Steps

### 1. Clone the repo and cd into the folder

```sh
git clone git@github.com:kenpfowler/coding-challenge-web-server.git

cd ./coding-challenge-web-server
```

### 2. Run the server

call your python interpreter with **program.py** as an argument.

example:

```sh
python program.py
```

You can also run the server with a desired hostname and port like this:

```sh
python ./program.py --host=localhost --port=8080
```

The server should respond with the following on startup

**2024-11-03 15:10:11,189 - INFO - server listening on localhost:8080**

### 3. make a request

The server runs on localhost:8080 by default. Access via command line with `curl` or via your browser.

```sh
curl http://localhost:8080
```

### 4. Shut down the server

Use Ctrl + C to shut down the server. It should respond with the following:

**2024-11-03 15:24:25,702 - INFO - gracefully shutting down server**

**2024-11-03 15:24:25,702 - INFO - server shutdown complete**
