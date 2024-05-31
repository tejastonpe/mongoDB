from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db=client['bridgelabz_training']
collection = db['students']

def insert_one_document():
    """
    Description: Insert one document in students collection
    Parameter  : None
    Return     : None
    """
    document={"name":"Ram","age":22,"city":"pune"}
    result=collection.insert_one(document)
    print(f"Inserted document ID: {result.inserted_id}")

def insert_many_document():
    """
    Description: Insert many documents in students collection
    Parameter  : None
    Return     : None
    """
    document=[{"name":"charan","age":14,"city":"ramwadi"},
              {"name":"chetan","age":33,"city":"kurla"},
              {"name":"khus","age":32,"city":"airoli"}]
    result=collection.insert_many(document)
    print(f"Inserted document IDs: {result.inserted_ids}")

def read_single_document():
    """
    Description: Retrive single document from students collection
    Parameter  : None
    Return     : None
    """
    result=collection.find_one({"name":"Ram"})
    print(result)

def read_multiple_document():
    """
    Description: Retrive multiple documents from students collection     whose age greater than 21.
    Parameter  : None
    Return     : None
    """
    result=collection.find({"age":{"$gt":21}})
    for i in result:
        print(i)

def update_single_document():
    """
    Description: updates single document in students collection
    Parameter  : None
    Return     : None
    """
    result=collection.update_one({"name":"lakhan"},{"$set":{"age":28}})
    print(f"Matched count: {result.matched_count}, Modified count: {result.modified_count}")

def update_multiple_document():
    """
    Description: updates multiple documents in students collection     whose age greater than 21.
    Parameter  : None
    Return     : None
    """
    result=collection.update_many({"city":"pune"},{"$set":{"city":"Mumbai"}})
    print(f"Matched count: {result.matched_count}, Modified count: {result.modified_count}")

def delete_single_document():
    """
    Description: delete single document from students collection
    Parameter  : None
    Return     : None
    """
    result=collection.delete_one({"name":"khus"})
    print(f"Deleted count: {result.deleted_count}")

def delete_multiple_document():
    """
    Description: delete multiple documents from students collection     whose age less than than 21.
    Parameter  : None
    Return     : None
    """
    result=collection.delete_many({"age":{"$lt":20}})
    print(f"Deleted count: {result.deleted_count}")

def main():    
    try:
        while True:
            print(f"\n1-Insert single document \n2-Insert multiple documents \n3-Read single document \n4-Read multiple documents \n5-Update single document \n6-Update multiple documents \n7-Delete single document \n8-Delete multiple documents \n9-Exit")
            inp=int(input("\nEnter operation no: "))
            match inp:
                case 1:
                    insert_one_document()
                case 2:
                    insert_many_document()
                case 3:
                    read_single_document()
                case 4:
                    read_multiple_document()
                case 5:
                    update_single_document()
                case 6:
                    update_multiple_document()
                case 7:
                    delete_single_document()
                case 8:
                    delete_multiple_document()
                case 9:
                    break
                case _:
                    print("Invalid option")    
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()