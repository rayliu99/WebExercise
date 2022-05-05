## Installation

Create a copy of this [template repo](https://github.com/prof-rossetti/daily-briefings-py), then clone or download your new repo onto your local computer (for example to the Desktop), and navigate there from the command-line:

```sh
cd ~/Desktop/daily-briefings-py/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "briefings-env":

```sh
conda create -n briefings-env python=3.8
conda activate briefings-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

## Web Application
```
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=web_app
flask run
```


## Testing

Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```


## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server and schedule the server to send you the weather forecast email every day.

## [License](/LICENSE.md)
