# QiuzzApp-FastAPI
### Installation Guide

# You need following to run this project:
console
 Python 3.11

# 1. Create a virtual environment using venv:

console
python -m venv name_of_env


# 2. Activate virtual env

console
./name_of_env/Scripts/activate


# 3. Install the dependencies:
   pip install fastapi
   pip install uvicorn
   pip install  psycopg2
   pip install sqlalchemy

# 4. Run the server:
Terminal command
uvicorn main:app --reload 

