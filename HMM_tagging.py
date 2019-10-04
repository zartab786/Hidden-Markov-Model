import re,pickle,string
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_begin","rb")
dict_begin=pickle.load(fp)
fp.close()
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_tag_count","rb")
dict_tag_count=pickle.load(fp)
fp.close()
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_tag2tag_count","rb")
dict_tag2tag_count=pickle.load(fp)
fp.close()
fp=open("E:\\Assignments\\NLP\\Assignment3\\pickle\\dict_word_tag_count","rb")
dict_word_tag_count=pickle.load(fp)
fp.close()

fp=open("E:\\Assignments\\NLP\\Assignment3\\testset2.txt","r")
text=fp.read()
fp.close()
sentences=sent_tokenize(text)
sentences=[i for i in sentences if i]
if(len(sentences)==0):
	print("Please enter valid text")
for sentence2 in sentences:
	sentence2=re.sub("\n"," ",sentence2)
	#print(sentence2)

	tokens2=sentence2.split()
	length=len(tokens2)
	if(tokens2[length-1]=='.'):
		length=length-1
	tokens=[""]
	for i in range(0,length):
			tokens.append(tokens2[i])
	#print(tokens)
	row,col=(37,len(tokens))
	viterbi=[[0]*col for i in range(37)]
	tags=[0]
	backpointer=[[0]*col for i in range(37)]
	for i in dict_tag_count.keys():
		tags.append(i)

	#print(tags)

	for i in range(1,len(tags)):
		if(len(tokens)>1):
			bigram=tokens[1]+" "+tags[i]
			#print(bigram)
			if(tags[i] in dict_begin.keys()):
				#print(tags[i])
				if(bigram in dict_word_tag_count.keys()):
					
					viterbi[i][1]=(dict_begin[tags[i]]/12950)*(dict_word_tag_count[bigram]/(dict_tag_count[tags[i]]+36))
				else:
					viterbi[i][1]=(dict_begin[tags[i]]/12950)*(1/(dict_tag_count[tags[i]]+36))	

			else:
				viterbi[i][1]=0

			backpointer[i][1]=0	
			
	#print(viterbi)
	bestpathprob=0
	bestpathpointer=0
	for t in range(2,len(tokens)):
		for s in range(1,len(tags)):
			bigram=tokens[t]+" "+tags[s]
			op=0

			if(bigram in dict_word_tag_count.keys()):
				op=(dict_word_tag_count[bigram]/(dict_tag_count[tags[s]]+1))
			else:
				op=(1/(dict_tag_count[tags[s]]+1))

			maximum=0	

			for s2 in range(1,len(tags)):
				bitag=tags[s2] +" "+tags[s]
				tp=0
				if(bitag in dict_tag2tag_count.keys()):
					tp=dict_tag2tag_count[bitag]/dict_tag_count[tags[s2]]

				hold=viterbi[s2][t-1]*tp*op	
				if hold>maximum:
					maximum=hold
					backpointer[s][t]=s2
					bestpathpointer=backpointer[s][t]
			viterbi[s][t]=maximum
			if(viterbi[s][t]>bestpathprob):
				bestpathprob=viterbi[s][t]


	#print(viterbi)
	#print(backpointer)		
	#print(bestpathprob)	
	#print(bestpathpointer)

	val=bestpathpointer
	dict_backtrack={}
	count=len(tokens)-1

	if len(tokens)>2:
		while val>0:
				dict_backtrack[tokens[count]]=tags[val]
				val=backpointer[val][count]
				count=count-1
		for i in range(1,len(tokens)):
			print(tokens[i],end="  ")
			print(dict_backtrack[tokens[i]])
		print(".",end=" ")
		print(".")	


		
	else:
		if(len(tokens)==2):
			max=0
			for i in range(1,len(tags)-1):
				bigram=tokens[1]+" "+tags[i]
				op=0
				if(bigram in dict_word_tag_count.keys()):
					op=(dict_word_tag_count[bigram]/(dict_tag_count[tags[i]]+1))
					if(op>max):
						max=op
						bestpathpointer=i
				else:
					op=(1/(dict_tag_count[tags[i]]+1))
					if(op>max):
						max=op
						bestpathpointer=1

			print(tokens[1],end="  ")
			print(tags[bestpathpointer])
			print(".",end=" ")
			print(".")

		







	





				

			
						













