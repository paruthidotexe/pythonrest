from tasksdata import Tasks

def GetStartedTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "started":
            TasksList.append(task)
    return TasksList


def GetDefaultTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "default":
            TasksList.append(task)
    return TasksList


def GetCompletedTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "completed":
            TasksList.append(task)
    return TasksList


def GetAllTasks():
    TasksList = []
    TasksList.extend(GetDefaultTasks())
    TasksList.extend(GetStartedTasks())
    TasksList.extend(GetCompletedTasks())
    # for task in TasksList:
    #     print ("\n" + str(task))
    return TasksList

    