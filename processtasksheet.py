import csv
from pymongo import MongoClient
import codecs
client = MongoClient()
db=client.quizdb
from time import gmtime, strftime
#print db
#username="tvpsir"
#coursename="cs315_1"
collection=db.questionbank
#collection_rec.insert({"ada":"dada"})
#collection_rec.find_one({u'username':username})["count"]=11
#print collection_rec
#count= collection_rec.find_one({"username":username})['count']
import shutil, errno
#print count
#print val
#defaultquestions=["Is this image profane or not?","Is this comment profane or not?", "Categorize this image into 5 categories","Categorize this book","Give 5 tags to this article","Give 5 tags for this image"," Which of the variants look good to you?","Which of the variants matches the description?","Is this ad appealing to you?","Grade the sentiment expressed in this tweet","Grade the sentiment expressed in this user comment","From the product review, is the customer satisfied?", "Which image is better?", "Which design is more soothing?","How will you rank this MP3 file?","Help us rate this place"]
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

import sys
import os
coursename=sys.argv[1]
coursename=coursename.replace("uploads/","")
coursename=coursename.replace(".csv","")
os.chdir("projects/")
#os.system("pwd")
os.system("cordova create "+coursename+" com.example.hello "+coursename)

root_src_dir = '../www/'
root_dst_dir = "../projects/"+coursename+"/www/"
shutil.rmtree("../projects/"+coursename+"/www/")
copyDirectory("../www/","../projects/"+coursename+"/www/")


fi=codecs.open(coursename+"/www/data.js","w",encoding="utf-8")
fi.write("var sampletask=[")
count=1
with open("../"+sys.argv[1], 'rb') as csvfile:
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
			post={"question":row[0],"option1":option1,"option2":option2,"option3":option3,"option4":option4,"answer":row[5],"coursename":coursename,"timelimit":int(row[6]),"index":count}
			fi.write(str(post)+",\n")	
			collection.insert(post)
			count=count+1
			
fi.write("]")
fi.close()
os.chdir("../projects/"+coursename)
os.system("cordova platform add android")
os.system("cordova build android")