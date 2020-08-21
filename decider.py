import json
import random
import os

debug = False

def isEligible(task, likes, limits, toys, anatomy):
    isNotLimit = not any([category in limits for category in task["categories"]])
    isLiked = any([category in likes for category in task["categories"]])
    hasToys = all([toy in toys for toy in task["toys"]])
    hasAnatomy = all([anatomyElement in anatomy for anatomyElement in task["anatomy"]])
    return isNotLimit and isLiked and hasToys and hasAnatomy

def findTasks():
    tasks = []
    for entry in os.scandir("tasks"):
        if (entry.path.endswith(".json") and entry.is_file()):
            with open(entry.path, "r") as task_file:
                fileContent = json.load(task_file)
            tasks.extend(fileContent)
    return tasks


def pickTask(likes, limits, toys, anatomy):
    tasks = findTasks()
    if(debug): print("found", len(tasks), "tasks")
    eligibleTasks = [task for task in tasks if isEligible(task, likes, limits, toys, anatomy)]
    if(debug): print("picking from", len(eligibleTasks), "eligible tasks")
    return eligibleTasks[random.randint(0,len(eligibleTasks) - 1)]

def buildTask(task):
    if(debug): print("building task ", task["text"])
    result = task["text"]
    for variable in task["variables"]:
        if(debug): print("building variable", variable["name"])
        value = ""
        if variable["type"] == "randomInt" :
            value = str(random.randint(variable["min"], variable["max"]))
        result = result.replace("[["+variable["name"]+"]]", value)
    return result

#TODO verify files conforming to schema
with open("config.json") as config_file:
    config = json.load(config_file)
result = buildTask(pickTask(
    config["likes"], 
    config["limits"], 
    config["toys"],
    config["anatomy"]
))
print(result)
