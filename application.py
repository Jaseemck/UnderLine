from flask import Flask, render_template
from newsapi import NewsApiClient

application = Flask(__name__)

@application.route("/")
def homepage():
    newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")
    #topheadlines = newsapi.get_everything(sources='bbc-news')
    topheadlines = newsapi.get_top_headlines(language='en')
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

@application.route("/in")
def ind():
    newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")
    #topheadlines = newsapi.get_everything(sources='bbc-news')
    topheadlines = newsapi.get_top_headlines(country='in',
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
    return render_template('india.html',context=mylist)

@application.route("/covid")
def cov():
    newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")
    #topheadlines = newsapi.get_everything(sources='bbc-news')
    topheadlines = newsapi.get_everything(q='covid',
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
    return render_template('covid.html',context=mylist)

@application.route("/biz")
def business():
    newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")
    #topheadlines = newsapi.get_everything(sources='bbc-news')
    topheadlines = newsapi.get_everything(q='business',
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
    return render_template('biz.html',context=mylist)

@application.route("/world")
def ever():
    newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")
    #topheadlines = newsapi.get_everything(sources='bbc-news')
    all_articles = newsapi.get_everything(
                                    sources='bbc-news,the-verge',
                                    language='en',
                                    sort_by='relevancy')
    articles = all_articles['articles']
    desc=[]
    news=[]
    img=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist = zip(news,desc,img)
    return render_template('world.html',context=mylist)

if __name__ == "__main__":
    application.run(debug=True)
