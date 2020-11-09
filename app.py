import json


def loadEventData():
    file = open("data/event.json")
    data = json.load(file)
    return data

def printEvent(data):
    print("#"*30)
    print(f"Event: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Guests: {len(data['guests'])}")
    print("#"*30)
    
def inviteGuest(data):
    name = input("Enter guest name: ")
    data["guests"].append(name)
    return data

def saveData(data):
    file = open("data/event.json","w")
    json.dump(data,file)
    file.close()
######################
### HW1: while/for + menu + if/else - interactive application + remove
data = loadEventData()
printEvent(data)
data = inviteGuest(data)
printEvent(data)
saveData(data)
    
