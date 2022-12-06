from fastapi import FastAPI
from nltk.tokenize import word_tokenize

words = ['fuck','hookup', 'hook-up', 'sex' , 'hook']

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

    flag=1
    blur = []
    tk = word_tokenize(message)
    for w in words:

        if(w in tk):
            flag=0
            blur.append(w)
            # break
    
    
    if flag==0:
        ff = 'Yes'
        dict1 = {ff:blur}
    else:
        ff = 'No'
        dict1 = {ff : blur}

    return dict1