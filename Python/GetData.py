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
		{'productname':'Mobile charger','category':'electronics','price':10,'color':'black'},
		{'productname':'Earphones','category':'accessories','price':90,'color':'blue'},
		{'productname':'Shoes','category':'accessories','price':500,'color':'black'},
		{'productname':'Bread','category':'food','price':15,'color':'white'},
		{'productname':'Notebook','category':'paper-products','price':7,'color':'white'},
		{'productname':'Jam','category':'food','price':125,'color':'red','storeLocation':{'lat':-83372,'long':9827}}
		]

#product_collection.insert_many(test_data) #-- commenting this to prevent multiple insertion of the same data
#to get all the data from collection  - select * from table

# -1 descending
#  1 ascending
all_records = product_collection.find().sort("productname", -1) # returns a cursor which can be looped through 

#0 means column will be excluded from result set 
#"_id" will be returned by default, to exclude it need to set 0 
selected_columns = product_collection.find({},{ "_id": 0, "productname": 1, "category": 1 })
for record in selected_columns:
	print(record)

#print(all_records)

for each_record in all_records: # loop through each record and prints the JSON document 
	print(each_record)

#to get the first record from the collection 

first_record = product_collection.find_one()
#print('JSON document: ',first_record)


#Get records by some filteration on the data

for record in product_collection.find({'productname':'Earphones'}):
	print('Earphones as productname:  ',record)

# Using Operators $in, $lt,$gt

for record in product_collection.find({'category':{'$in':['electronics','food']}}):
	print('category is either electronics or food ',record)

for record in product_collection.find({'$and':[{'color':'white'},{'category':'paper-products'}]}):
	print('having white color and belongs to paper-products :',record['productname']) #prints product name - retrieving data from dictionary using key

for record in product_collection.find({'$or':[{'price':'500'},{'category':'accessories'}]}): # 500 is given as string but it automatically compared with int property
	print('either having 500 as price or belongs to accessories :',record['productname']) #prints product name - retrieving data from dictionary using key


for record in product_collection.find({'category':'accessories','price':{'$lt':100}}):
	print('category is accessories and price less  than $100 ',record)


#qurying nested objects 

for record in product_collection.find({'storeLocation':{'lat':-83372,'long':9827}}):
	print('storeLocation lat:-83372, long:9827 :  ',record)


