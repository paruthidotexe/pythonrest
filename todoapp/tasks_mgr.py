from tasks_data import Tasks

def GetStartedTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "Started":
            TasksList.append(task)
    return TasksList


def GetDefaultTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "Default":
            TasksList.append(task)
    return TasksList


def GetCompletedTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "Completed":
            TasksList.append(task)
    return TasksList


def GetArchivedTasks():
    TasksList = []
    for task in Tasks:
        if task["state"] == "Archived":
            TasksList.append(task)
    return TasksList


def GetAllTasks():
    TasksList = []
    TasksList.extend(GetStartedTasks())
    TasksList.extend(GetDefaultTasks())
    TasksList.extend(GetCompletedTasks())
    TasksList.extend(GetArchivedTasks())
    
    # for task in TasksList:
    #     print ("\n" + str(task))
    return TasksList

    