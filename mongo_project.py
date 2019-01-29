import pymongo
import os

MONGO_URI = os.getenv("MONGO_URI")
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter an option: ")
    return option
    
def get_record():
    print("")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    
    try:
        doc = coll.find_one({'first_name': first_name.lower(), 'last_name': last_name.lower()})
    except:
        print("Error accessing the database")
        
    if not doc:
        print("")
        print("Error: NO results found")
        
    return doc

def add_record():
    print("")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    dob = input("Enter Date of Birth: ")
    gender = input("Enter Gender: ")
    hair_colour = input("Enter Hair Colour: ")
    occupation = input("Enter Occupation: ")
    nationality = input("Enter Nationality: ")
    
    new_doc = {'first_name': first_name.capitalize(), 'last_name': last_name.capitalize(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document Inserted")
    except:
        print("Error accessing the database")
        
def find_record():
    doc = get_record()
    if doc:
        print("")
        #k and v stands for keys and values
        for k,v in doc.items():
            #_id is the automatically generated mLab id for each entry into the database. Therefore the following line means that this will not be shown when the user requests to see an entry.
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                
                if update_doc[k] == "":
                    update_doc[k] == v
                    
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document was Updated")
        except:
            print("Error accessing the database")
            
def delete_record():
    
    doc = get_record()
    
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                    
        print("")
        confirmation = input("Are you sure this is the document you want to delete?\nY or N ")
        print("")
            
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document Deleted")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")

def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            find_record()
        elif option == '3':
            edit_record()
        elif option == '4':
            delete_record()
        elif option == '5':
            conn.close()
            break
        else:
            print("Incorrect Answer")
        print("")
            
conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()