from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
# here flask work for data extraction from any site 
def index():
    url="https://www.goodhousekeeping.com/health/wellness/g2401/inspirational-quotes/"

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    # parentmain = soup.find_all('div' ,class_="listicle-slide" , limit=7)  #you can make parentmain variable then use in loop as a variable.
    finalquto=""

    for data in soup.find_all('div' ,class_="listicle-slide" ,limit=5):
    #strip-> we are using strip because when we print data there is lots of space between the date so remove this unwanted date we use strip
    #.text -> without text we can't be able to print the date which was print in p tag
        quto=data.find('div' ,class_="listicle-slide-dek").text.strip()
        finalquto += '\u2023 '+quto+'\n'
    #print(finalquto)
    return render_template("index.html", News =finalquto)


#  Set-ExecutionPolicy Unrestricted -Scope Process  ->first run this command into terminal for run flask then
# venu/Scripts/activate 
# flask run


