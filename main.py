import pymongo
# CRUD OPERATION : (CREATE, READ, UPDATE, DELETE)
#1. Insert Operation :
# BULK INSERTING A DOCUMENT / CREATE A DOCUMENT
def bulkInsert():
    studentInfo_bulk = [{
        "name": "Sajid",
        "section": 1,
        "maths_marks": 98,
        "science_marks": 99
    },
    {
        "name": "Saad",
        "section": 2,
        "maths_marks": 71,
        "science_marks": 95
    },
    {
        "name": "Shafi",
        "section": 1,
        "maths_marks": 78,
        "science_marks": 90
    },
    {
        "name": "Faizan",
        "section": 1,
        "maths_marks": 57,
        "science_marks": 56
    },
    {
        "name": "Junaid",
        "section": 2,
        "maths_marks": 48,
        "science_marks": 37
    },
    {
        "name": "Danish",
        "section": 2,
        "maths_marks": 68,
        "science_marks": 45
    }]
    student_id = collection.insert_many(studentInfo_bulk)
    print(f"Student with id {student_id} has been created.")

# INSERTING A DOCUMENT / CREATE A DOCUMENT
def insertDocument():
    studentInfo = {
        "name": "Sajid",
        "section": 1,
        "maths_marks": 98,
        "science_marks": 99
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f"Student with id {student_id} has been created.")

# 2. Update Operation
#UPDATE ONE  ----> Will Update only 1 Result
def updateOne():
    collection.update_one({"section":1},{'$inc':{"section":100}})  # '$inc'---> Increment By
    collection.update_one({"section": 1}, {'$set': {"section": 500}})  # '$set'---> Set Single Value
    collection.update_one({"section": 1}, {'$unset': {"section": ""}})  # '$unset'---> UnSet Single Value

#UPDATE MANY   ----> Will update all the Results.
def updateMany():
    collection.update_many({"section": 1}, {'$inc': {"section": 100}})  #'$inc'---> Increment By
    collection.update_many({"section": 1}, {'$set': {"section": 500}})  # '$set'---> Set Many Values
    collection.update_many({"section": 2}, {'$unset': {"section": "" }})  # '$unset'---> UnSet Many Values

# 3. DELETE OPERATION
#DELETE ONE  ----> Will Delete only 1 Result
def deleteOne():
    collection.delete_one({"section":2})

#DELETE MANY   ----> Will Delete all the Results.
def deleteMany():
    collection.delete_many({"section": 1})
    # collection.delete_many({})   #This will Delete Entirely.

# 4. Read Operation
# READ OPERATION -->  USING FIND METHOD
def readDocument():
    myStudents = collection.find({})  # This will find everything.
    # Here, we can find a specific / filter according to requirement as below:
    # myStudents = collection.find({"section": 2})
    # myStudents = collection.find({"section" : 2, "name" : "Sajid"})
    # Using find_one()   ..... Will Fetch only One Result
    # myStudents = collection.find_one({"section": 1,"name" : "Sajid"})
    print(myStudents)
    for student in myStudents:
        print(student)

if __name__ == "__main__":
    client = pymongo.MongoClient('localhost:27017')
    #Creating a Database for a School.
    db = client['RMV_School']
    #Creating a Collection
    collection = db.class1
    # insertDocument()  --> Whenever we have to Bulk Insert, we have to give a JSON Format Dictionary in the form of List
    bulkInsert()
    readDocument()
    # updateOne()
    # updateMany()
    # deleteOne()
    # deleteMany()