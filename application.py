from flask import Flask, render_template
from newsapi import NewsApiClient

application = Flask(__name__)

@application.route("/")
def homepage():
    newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")
    #topheadlines = newsapi.get_everything(sources='bbc-news')
    topheadlines = newsapi.get_top_headlines(q='covid',
                                      country='in',
                                      language='en')
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('index.html',context=mylist)

if __name__ == "__main__":
    application.run(debug=True)
