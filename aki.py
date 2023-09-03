import numpy as np
import pandas as pd
import random

df = pd.read_csv("https://raw.githubusercontent.com/kbpoovanna-007/IMDB-AKINATOR/main/imdb_top_1000.csv")

Genres = {}
actors = {}
certificate = {}
directors = {}

def take_out():
	genres = df["Genre"].str.split(expand = True)
	genres = genres.replace(',','',regex = True)
	Genres = set(genres[0]).union(set(genres[1])).union(set(genres[2]))
	Genres.remove(None)

	certificate = set(df["Certificate"])
	directors = set(df["Director"])

	actors = df[['Star1','Star2','Star3','Star4']]
	actors = set(actors['Star1']).union(set(actors['Star2'])).union(set(actors['Star3'])).union(set(actors['Star4']))
	return actors,certificate,directors,Genres,genres

def questioning():
	
	#actors,certificate,directors,Genres = take_out()
	actor = random.choice(tuple(actors))
	cf = random.choice(tuple(certificate))
	director = random.choice(tuple(directors))
	genre = random.choice(tuple(Genres))
	Questions = ["Is "+str(actor)+" in the movie?",
	             "Is the movie rated "+str(cf)+"?",
	             "Is "+str(director)+" The Director of the movie?",
	             "Does "+str(genre)+" describe your movie?"]
	i = Questions.index(random.choice(Questions))
	return i,Questions[i],actor,cf,director,genre

asf = 0
cf = 0
dirf = 0
gen = 0

while(len(df.axes[0])>1):

	actors,certificate,directors,Genres,genres = take_out()
	ind,question,actor,certi,director,genr = questioning()
	if((asf>4 and ind == 0) or (cf>0 and ind == 1) or (dirf>0 and ind == 2) or (gen>3 and ind == 3)):
		continue
	print(question)
	ans = input("Yes or No: ")
	if(ind == 0):
	    actors.remove(actor)
	    if(ans == "Yes"):
	        for ind in df.index:
	            if(df['Star1'][ind]!=actor and df['Star2'][ind]!=actor and df['Star3'][ind]!=actor and df['Star4'][ind]!=actor):
	                df = df.drop(ind)  
	                asf = asf+1  
	    else:
	        for ind in df.index:
	            if(df['Star1'][ind]==actor and df['Star2'][ind]==actor and df['Star3'][ind]==actor and df['Star4'][ind]==actor):
	                df = df.drop(ind)

	elif(ind == 1):
	    certificate.remove(certi)
	    if(ans == "Yes"):
	        for ind in df.index:
	            if(df['Certificate'][ind]!=certi):
	                df = df.drop(ind)
	                cf = cf+1
	    else:
	        for ind in df.index:
	            if(df['Certificate'][ind]==certi):
	                df = df.drop(ind)

	elif(ind == 2):
	    directors.remove(director)
	    if(ans == "Yes"):
	        for ind in df.index:
	            if(df['Director'][ind]!=director):
	                df = df.drop(ind)
	                dirf = dirf+1
	    else:
	        for ind in df.index:
	            if(df['Director'][ind]==director):
	                df = df.drop(ind)

	elif(ind == 3):
	    Genres.remove(genr)
	    if(ans == "Yes"):
	        for ind in df.index:
	            if(genres[0][ind]!=genr and genres[1][ind]!=genr and genres[2][ind]!=genr):
	                df = df.drop(ind)
	                genres = genres.drop(ind)
	    else:
	        for ind in df.index:
	            if(genres[0][ind] == genr and genres[1][ind] == genr and genres[2][ind] == genr):
	                df = df.drop(ind)
	                genres = genres.drop(ind)

if df.empty:
	print("There is no movie like this")
else:	
	print(df['Series_Title'])
                                            