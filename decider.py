import json
import random

def pickTask(likes, limits, toys):
    with open("tasks.json", "r") as task_file:
        tasks = json.load(task_file)
    #TODO filter tasks for eligibility

    eligibleTasks = tasks
    return eligibleTasks[random.randint(0,len(eligibleTasks) - 1)]

def buildTask(task):
    result = task["text"]
    for variable in task["variables"]:
        value = ""
        if variable["type"] == "randomInt" :
            value = str(random.randint(variable["min"], variable["max"]))
        result = result.replace("[["+variable["name"]+"]]", value)
    return result

#TODO verify files conforming to schema
with open("config.json") as config_file:
    config = json.load(config_file)
result = buildTask(pickTask(config["likes"], config["limits"], config["toys"]))
print(result)
