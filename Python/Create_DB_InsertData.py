# mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb

import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

blog_db = client['BlogDB']

blog_collection = blog_db.BlogData

blog_post = {
	'title':'Blog 1 title',
	'Desc':'Description of the blog goes here'
}

blog_id = blog_collection.insert_one(blog_post)
print(blog_id._id)

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

blog_ids= blog_collection.insert_many(multiple_blog_post)
print(blog_ids)