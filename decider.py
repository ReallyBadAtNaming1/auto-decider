import json
import random

def isEligible(task, likes, limits, toys):
    isNotLimit = not any([category in limits for category in task["categories"]])
    isLiked = any([category in likes for category in task["categories"]])
    hasToys = all([toy in toys for toy in task["toys"]])
    return isNotLimit and isLiked and hasToys

def pickTask(likes, limits, toys):
    with open("tasks.json", "r") as task_file:
        tasks = json.load(task_file)
    eligibleTasks = [task for task in tasks if isEligible(task, likes, limits, toys)]
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
