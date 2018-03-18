from flask import Flask
import json

app = Flask(__name__)


def GetAllTasks():
    Tasks =[
        {
            "id" : 1,
            "desc" : "LAN server",
        },
        {
            "id" : 2,
            "desc" : "oAuth verifications",
        },
        {
            "id" : 3,
            "desc" : "ToDo List App",
        },
        {
            "id" : 4,
            "desc" : "Admin App",
        },
        {
            "id" : 5,
            "desc" : "Database Integration",
        }
    ]
    return Tasks


@app.route("/")
def home():    
    return "Task Lists"


@app.route("/tasks")
def AllTasks():    
    return json.dumps(GetAllTasks())


if __name__ == "__main__":    
    app.run(host= '0.0.0.0', port=7777)
