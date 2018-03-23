from flask import Flask
from flask import render_template
import json
import tasksmgr 


app = Flask(__name__)


@app.route("/")
def IndexPage():
    return render_template("index.html")


@app.route("/api/v1/tasks")
def GetAllTasksApi():    
    return json.dumps(tasksmgr.GetAllTasks())


@app.route("/api/v1/tasks/completed")
def GetCompletedTasksApi():    
    return json.dumps(tasksmgr.GetCompletedTasks())


@app.route("/api/v1/tasks/started")
def GetStartedTasksApis():    
    return json.dumps(tasksmgr.GetStartedTasks())


@app.route("/api/v1/tasks/default")
def GetDefaultTasksApi():    
    return json.dumps(tasksmgr.GetDefaultTasks())


@app.route("/tasks")
def HomePage():    
    return render_template("tasks.html", tagVal = "All Tasks", taskList = tasksmgr.GetAllTasks())


@app.route("/tasks/completed")
def GetCompletedTasks():    
    return render_template("tasks.html", tagVal = "Completed", taskList = tasksmgr.GetCompletedTasks())


@app.route("/tasks/started")
def GetStartedTasks():    
    return render_template("tasks.html", tagVal = "Started", taskList = tasksmgr.GetStartedTasks())


@app.route("/tasks/default")
def GetDefaultTasks():    
    return render_template("tasks.html", tagVal = "Default", taskList = tasksmgr.GetDefaultTasks())


if __name__ == "__main__":    
    app.run(debug=True, host= '127.0.0.1', port=7777)




