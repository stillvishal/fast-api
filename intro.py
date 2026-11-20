from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
        return data


@app.get("/")
def hello():
    return ({"message": "Patient Management System API is running."})

@app.get("/about")
def about():
    return ({"message": "Fully functional Patient Management System API built with FastAPI."})

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
def view_patient(patient_id):
    data = load_data()
    















