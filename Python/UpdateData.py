# mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
# Get data from mongo db - Querying- similar to where queries in Relational Database
# Refer Create_DB_InsertData.py file for create database and inserting into mongodb collection
# uncomment product_collection.insert_many(test_data) to insert data and comment it to prevent duplicate records insertion

import pymongo

#Connecting to mongodb
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

#creates database named 'ProductsDB' if not already exist
#uses this database for further operations
product_db = client['ProductsDB']

#Creating a collection to store data (Similar to table in Relation DB)
product_collection = product_db.ProductData

test_data = [
		{'productname':'Mobile charger','category':'electronics','price':10,'color':'black','storeLocation':{'lat':-734,'long':234}},
		{'productname':'Earphones','category':'accessories','price':90,'color':'blue','storeLocation':{'lat':-9434,'long':1343}},
		{'productname':'Shoes','category':'accessories','price':500,'color':'black','storeLocation':{'lat':-423,'long':23443}},
		{'productname':'Bread','category':'food','price':15,'color':'white','storeLocation':{'lat':-2545,'long':23342}},
		{'productname':'Notebook','category':'paper-products','price':7,'color':'white', 'storeLocation':{'lat':-8927,'long':1221}},
		{'productname':'Jam','category':'food','price':125,'color':'red','storeLocation':{'lat':-83372,'long':9827}}
		]

product_collection.insert_many(test_data) #-- commenting this to prevent multiple insertion of the same data
#to get all the data from collection  - select * from table

all_records = product_collection.find() # returns a cursor which can be looped through 

#print(all_records)

for each_record in all_records: # loop through each record and prints the JSON document 
	print(each_record)


#update one record 
# after update : {'productname':'Jam','category':'food','price':125,'color':'pink','storeLocation':{'lat':-83372,'long':100000},'lastUpdated':'2020-05-15T19:50:37.254+00:00'}

product_collection.update_one(
	{'productname':'Jam'},
	{'$set':{'storeLocation.long':100000,'color':'pink'},'$currentDate':{'lastUpdated':True}}
	)

#all electronics items will be updated 
product_collection.update_many(
	{'category':'electronics'},
	{'$set':{'storeLocation.lat':888888888,'color':'black'},'$currentDate':{'lastUpdated':True}}
	)


product_collection.replace_one(
	{'productname':'Bread'},
	{'newProdu':'item1','NestedValue':[{'nested1':'hello'},{'nested2':'Awesome'}], 'storeLocation':{'lat':982727,'long':{'sublong':'sub value'}}}
	)
