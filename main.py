from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key="86169c5e6d3f48da8dc3f9402c6efbb9")

@app.route("/")
def homepage():
    topheadlines = newsapi.get_top_headlines(language='en')
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
    mylist = zip(news,desc,img,url)
    return render_template('index.html',context=mylist)

@app.route("/in")
def ind():
    topheadlines = newsapi.get_top_headlines(country='in',
                                      language='en')
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
    mylist = zip(news,desc,img,url)
    return render_template('india.html',context=mylist)

@app.route("/covid")
def cov():
    topheadlines = newsapi.get_everything(q='covid',
                                    language='en')
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
    mylist = zip(news,desc,img,url)
    return render_template('covid.html',context=mylist)

@app.route("/biz")
def business():
    topheadlines = newsapi.get_everything(q='business',
                                    language='en')
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
    mylist = zip(news,desc,img,url)
    return render_template('biz.html',context=mylist)

@app.route("/world")
def ever():
    all_articles = newsapi.get_everything(
                                    sources='bbc-news,the-verge',
                                    language='en',
                                    sort_by='relevancy')
    articles = all_articles['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
    mylist = zip(news,desc,img,url)
    return render_template('world.html',context=mylist)

if __name__ == "__main__":
    app.run(debug=True)
