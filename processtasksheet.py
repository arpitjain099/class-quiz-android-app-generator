import csv
from pymongo import MongoClient
import codecs
client = MongoClient()
db=client.quizdb
from time import gmtime, strftime
collection=db.tasks
#print db
username="tvpsir"
coursename="cs315"
collection=db.questionbank
#collection_rec.insert({"ada":"dada"})
#collection_rec.find_one({u'username':username})["count"]=11
#print collection_rec
#count= collection_rec.find_one({"username":username})['count']

#print count
#print val
#defaultquestions=["Is this image profane or not?","Is this comment profane or not?", "Categorize this image into 5 categories","Categorize this book","Give 5 tags to this article","Give 5 tags for this image"," Which of the variants look good to you?","Which of the variants matches the description?","Is this ad appealing to you?","Grade the sentiment expressed in this tweet","Grade the sentiment expressed in this user comment","From the product review, is the customer satisfied?", "Which image is better?", "Which design is more soothing?","How will you rank this MP3 file?","Help us rate this place"]
fi=codecs.open("data.js","w",encoding="utf-8")
fi.write("var sampletask=[")
with open('inputdata.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	#spamreader=spamreader[17:]
	for index,row in enumerate(spamreader):
		if index > 0:
			option1=row[1]
			option2=row[2]
			option3=row[3]
			option4=row[4]
			if row[0]=='':
				option1="N/A"
			if row[2]=='':
				option2="N/A"
			if row[3]=='':
				option3="N/A"
			if row[4]=='':
				option4="N/A"
			post={"question":row[0],"option1":option1,"option2":option2,"option3":option3,"option4":option4,"answer":row[5],"coursename":coursename}
			fi.write(str(post)+",\n")	
			collection.insert(post)
			
fi.write("]")
fi.close()