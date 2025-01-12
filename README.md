# LALA Now

## Project Overview

LALA now is a chatbot that provides information to those affected by Los Angeles Wildfires and people willing to assist.

## Local Development Set up
You should have Python 3.10 installed on your system.

### Create an .env file.
```bash
cp .env-example .env
```

The `API_ENV` environmental variable determines whether the API requires an `API_KEY` to validate requests.  When set to either `staging` or `production`, the token is necessary.  Otherwise, it is not necessary.

The `DATABASE_URL` is required.  The `.env-example` has a reference to a local postgres database.

```bash
API_KEY=
API_ENV="local_dev"
DATABASE_URL="postgresql://postgres:password@postgres:5432/postgres"
```

### Run the application manually
Set up a virtual environment.
```bash
python -m virtualenv .venv

source .venv/bin/activate
```

Install Python dependencies.
```bash
python -m pip install --upgrade pip poetry
```

Install the API-specific dependencies.
```bash
python -m poetry install
```
Start the application.  You can add the `--reload` flag to this command to restart the server upon saving the app.
```bash
gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker
```

On Windows, you can run the app using `uvicorn`:
```bash
uvicorn app.main:app --host 127.0.0.1 --reload
```


### Interact with the ORM layer
You can interact with the ORM layer directly using regular Django commands, as well as custom Django commands.  

#### View available commands
```bash
python -m app help
```

#### Create/Update database
```bash
# Create new migrations if you added/updated models
python -m app makemigrations
python -m app migrate
```

### Run Tests
```bash
pytest
```


## Directory Structure
```bash
├── lalanow-backend
│   ├── .github # CICD workflow files that run in GitHub
│   ├── app
│   │   ├── data # Store dataset files like CSVs for testing, configuration, or analysis.
│   │   ├── django_orm # A set of tools to interact with a postgres database
│   │   │   ├── content
│   │   │   │   ├── management # Custom commands using "python -m app ____"
│   │   │   │   ├── migrations # History of database changes
│   │   │   │   ├── models.py # Where you define postgres database tables
│   │   │   ├── settings.py # Configures a minimal version of Django focused on the ORM
│   │   ├── routers # Endpoint files
│   │   │   ├── resources_nearby.py
│   │   ├── schemas # Request / response data structures for validation
│   │   │   ├── resources_nearby.py
│   │   ├── services # Core functionalities for the chatbot operations
│   │   ├── tests # Tests to validate the API's operation
│   │   │   ├── chats
│   │   │   │   ├── utils # A folder of reusable functions for tests
│   │   │   ├── conftest.py # Settings for all test suites
│   │   ├── constants.py # Configuration variables for the application
│   │   ├── dependencies.py # Reusable logic for use across multiple endpoints
│   │   ├── main.py # FastAPI application starting point
│   │   ├── enums.py # Holds consistent, reusable sets of related values
│   │   ├── flow_copy.py # Holds static, non-LLM copy for flows, like greetings or follow-ups
├── CHANGELOG.md
├── pyproject.toml # Project settings and dependencies
```
