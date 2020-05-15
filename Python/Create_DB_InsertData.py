# mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb

import pymongo

#Connecting to mongodb
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

#creates database named 'BlogDB' if not already exist
#uses this database for further operations
blog_db = client['BlogDB']

#Creating a collection to store data (Similar to table in Relation DB)
blog_collection = blog_db.BlogData


#Preaparing JOSON document to insert into the collection
blog_post = {
	'title':'Blog 1 title',
	'Desc':'Description of the blog goes here'
}

#inserting single record in the collection. Returns object which contains inserted record information
blog_id = blog_collection.insert_one(blog_post)
print(blog_id._id)

#preparing multiple records to intsert into the collection s
multiple_blog_post = [{
	'title':'Blog 3 title',
	'Desc':'Description of the blog goes here'
	}, 
	{
	'title':'Blog 4 title',
	'Desc':'Description of the blog goes here',
	'website':'https://midni8coder.blogspot.com'
	}
	]

#inserting multiple records 
blog_ids= blog_collection.insert_many(multiple_blog_post)
print(blog_ids)

