# importing api 
from newsapi import NewsApiClient
from django.shortcuts import render 


# Create your views here. 
def index(request): 
	
	newsapi = NewsApiClient(api_key ='007f9ea5d0674c44840e2db3a12a0931') 
	top = newsapi.get_top_headlines(sources ='techcrunch') 

	l = top['articles'] 
	desc =[] 
	news =[] 
	img =[] 

	for i in range(len(l)): 
		f = l[i] 
		news.append(f['title']) 
		desc.append(f['description']) 
		img.append(f['urlToImage']) 
	mylist = zip(news, desc, img) 

	return render(request, 'index.html', context ={"mylist":mylist}) 


