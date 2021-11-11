from sqlalchemy import create_engine, Table, Column,Integer, String, MetaData

engine = create_engine("sqlite:///mydb1.db", echo = True)
meta = MetaData()
data = Table(
   'StudData', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String),
   Column('degree', String),
   Column('sem', String),
   Column('branch', String),
)
meta.create_all(engine)

conn = engine.connect()

def create():
    N=int(input("Enter the number of student's details to be entered: "))
    for i in range(N):
        sName = input("Enter name: ")
        sDegree = input("Enter the Degree: ")
        sSem = input("Enter the Sem: ")
        sBranch = input("Enter the Branch: ")
        
        result = conn.execute(data.insert(),[
            {'name' : sName, 'degree' : sDegree, 'sem' : sSem, 'branch' : sBranch}
        ])

def read():
    s = data.select()
    result = conn.execute(s)
    for row in result:
        print (row)

def update():
    option = input("""Enter the parameter to be updated: 
                   Name
                   Degree
                   Sem
                   Branch: """)
    option = option.lower()
    optionList = ['name', 'degree', 'sem', 'branch']
    id = input("Enter the id of the student: ")
    if(option == optionList[0]):
        new = input("Enter the new "+ option +" : ")
        updated = data.update().where(data.c.id==id).values(name = new)
        result = conn.execute(updated)
        read()
    elif(option == optionList[1]):
        new = input("Enter the new "+ option +" : ")
        updated = data.update().where(data.c.id==id).values(degree = new)
        result = conn.execute(updated)
        read()
    elif(option == optionList[2]):
        new = input("Enter the new "+ option +" : ")
        updated = data.update().where(data.c.id==id).values(sem = new)
        result = conn.execute(updated)
        read()
    elif(option == optionList[3]):
        new = input("Enter the new "+ option +" : ")
        updated = data.update().where(data.c.id==id).values(branch = new)
        result = conn.execute(updated)
        read()

def delete():
    print("Do you wish to a single entry or a range of entries?")
    outer = int(input("Press 1 for single entry deletion:\nPress 2 for range of entries deletion: "))
    if(outer == 1):
        option = int(input("Enter the id of the element to be deleted: "))
        deleted = data.delete().where(data.c.id == option)
        result = conn.execute(deleted)
        read()
    elif(outer == 2):
        optionentry = int(input("Enter the starting ID of the range: "))
        optionexit = int(input("Enter the last ID of the range: "))
        deleted = data.delete().where((data.c.id >= optionentry) & (data.c.id <= optionexit) )
        result = conn.execute(deleted)
        read()

operation_dict = {1: create, 2: read, 3: update, 4: delete}

while(True):
    operation = int(input("""To perform the following operations: 
          Press 1 to enter new values:
          Press 2 to view the table: 
          Press 3 to update the records: 
          Press 4 to delete a record: """))
    performing = operation_dict[operation]() 
   

        