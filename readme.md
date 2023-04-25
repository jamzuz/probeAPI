## how to install

### *this project has been made with python 3.10
### first setup your virtual enviroment if you dont want to install everything globally
### Note: Project currently contains the PROBEapi_db.db file which contains mockdata, if you would like to run the api without data just delete the file and start the program again.
### install steps: 

`start/activate venv`
`navigate to \probeAPI folder`
1. `pip install fastapi uvicorn sqlalchemy`
2. `uvicorn app.main:app --reload` make sure you are in the probeAPI folder!!
3. `follow http link from the terminal and go to /docs (probably: "http://127.0.0.1:8000/docs")`
