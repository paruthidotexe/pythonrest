from flask import Flask
import json
import tasksmgr 

app = Flask(__name__)


@app.route("/")
def home():    
    return "Task Lists"


@app.route("/tasks")
def AllTasks():    
    return json.dumps(tasksmgr.GetAllTasks())


@app.route("/tasks/completed")
def GetCompletedTasksApi():    
    return json.dumps(tasksmgr.GetCompletedTasks())


@app.route("/tasks/started")
def GetStartedTasksApis():    
    return json.dumps(tasksmgr.GetStartedTasks())


@app.route("/tasks/default")
def GetDefaultTasksApi():    
    return json.dumps(tasksmgr.GetDefaultTasks())


if __name__ == "__main__":    
    app.run(host= '127.0.0.1', port=7777)
