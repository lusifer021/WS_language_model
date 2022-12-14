from fastapi import FastAPI
from nltk.tokenize import word_tokenize
from utils import words
import nltk
nltk.download('popular')
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.stem import WordNetLemmatizer
  
lemmatizer = WordNetLemmatizer()
# words = ['fuck','hookup', 'hook-up', 'sex' , 'hook']

app = FastAPI()

from pydantic import BaseModel

class Msg(BaseModel):
    message: str

@app.get("/")
def test():
        return {"working"}

@app.post("/detect")
async def detect(item: Msg):
    message = item.message

    token = word_tokenize(message)
    tokens = [x.lower() for x in word_tokenize(message)]

    flag =1
    message2 = ""
    for w in enumerate(tokens):
        
        # print(w)
        if ps.stem(w[1]) in words:
            flag=0
            message2 = message2 + "*" * len(w[1]) + " "
        elif lemmatizer.lemmatize(w[1]) in words:
            flag = 0
            message2 = message2 + "*" * len(w[1]) + " "
        elif w[1] in words:
            flag = 0
            message2 = message2 + "*" * len(w[1]) + " "
        else:
            message2 = message2 + token[w[0]] + " "

    
    if flag==0:
        ff = 'Yes'
        dict1 = {"Status":ff, "Message" : message2}
    else:
        ff = 'No'
        dict1 = {"Status":ff, "Message" : message2}

    return dict1