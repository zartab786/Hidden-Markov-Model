import re,string,pickle
from nltk.tokenize import sent_tokenize
fp=open("E:\\Assignments\\NLP\\Assignment3\\Trainingset_HMM.txt","r")
text=fp.read()
sentences=sent_tokenize(text)
fp.close()
#print(sentences)

dict_begin={}
dict_tag_count={}
dict_word_tag_count={}
dict_tag2tag_count={}
list_of_sentences=[]
for sentence in sentences:
	sentence=re.sub("\n"," ",sentence)
	sentence=re.sub("\t"," ",sentence)
	list_of_sentences.append(sentence.split())
	#print(sentence)
	#print(sentence[1])


#print(list_of_sentences)

for sentence in list_of_sentences:
	if len(sentence)>1:
		if sentence[1] in dict_begin.keys():
			dict_begin[sentence[1]]+=1
		else:
			dict_begin[sentence[1]]=1

	for i in range(0,len(sentence)):

		if sentence[i] =="my":
			if "PRP$" in dict_tag_count.keys():
				dict_tag_count["PRP$"]+=1
			else:
				dict_tag_count["PRP$"]=1	

		if sentence[i] in re.findall(r"[A-Z]+|;|[\.]",str(sentence)):

			if sentence[i] in dict_tag_count.keys():
					dict_tag_count[sentence[i]]+=1
			else:
				dict_tag_count[sentence[i]]=1

	
	for i in range(0,len(sentence)-1):
		if(i%2 ==0):

			word_tag=sentence[i] + " " +sentence[i+1]
			if word_tag in dict_word_tag_count.keys():
				dict_word_tag_count[word_tag]+=1
			else:
				dict_word_tag_count[word_tag]=1

	
	for i in range(1,len(sentence)-2):

		if(i%2 !=0):
			tag_tag=sentence[i] +" "+sentence[i+2]
			if tag_tag in dict_tag2tag_count.keys():
				dict_tag2tag_count[tag_tag]+=1
			else:
				dict_tag2tag_count[tag_tag]=1	




	


		


	
#print(dict_begin)
#print(dict_tag_count)
#print(dict_word_tag_count)
#print(dict_tag2tag_count)
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_begin","wb")
pickle.dump(dict_begin,fp)
fp.close()
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_tag_count","wb")
pickle.dump(dict_tag_count,fp)
fp.close()
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_word_tag_count","wb")
pickle.dump(dict_word_tag_count,fp)
fp.close()
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_tag2tag_count","wb")
pickle.dump(dict_tag2tag_count,fp)
fp.close()



total_start=0
for value in dict_begin.keys():
	total_start+=dict_begin[value]

print(total_start)	



