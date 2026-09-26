from datetime import datetime
task_db = []


task_id = 0

def create_task(title, description, dueration):
    global task_id 
    task_id+=1
    task = {
       "task_id": task_id,
       "title":title,
       "description": description,
       "dueration": dueration,
       "status": False,
       "created_at": datetime.now()
    }
    task_db.append(task)


def read_task(task_id):
    for i in task_db:
        if i["task_id"] == task_id:
            print(f"""
Your task {i["task_id"]}:
Title:{i["title"]}
Description:{i["description"]}
Dueration :{i["dueration"]}
Status:{i["status"]}
                  """)
 





while True:
    n = int(input("1)Create Task\n2)Read task\n3)Update Task\n4)Delete\n0)Exit\nChouse one: "))
    match n:
        case 1:
            print("Start create task") 
            title = input("Title: ")
            descp = input("Description: ")
            durat = input("Duration: ")            
            create_task(title, descp, durat) 
            print("Task created !!")
            
        case 2:
            k = int(input("Enter id task: "))
            read_task(k)
        case 3:
            pass
        case 4:
            pass
        case 0:
            print("Exit")
            break
        case _:
            print("Invalid input!")
            
            
            
print(task_db)
              