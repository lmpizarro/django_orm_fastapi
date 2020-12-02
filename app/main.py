import init
from app_01.models import Logger
from fastapi import  File, UploadFile
from fastapi import FastAPI, Form
from asgiref.sync import sync_to_async
from fastapi.responses import FileResponse

from pydantic import BaseModel


app = FastAPI()

'''
https://amitness.com/2020/06/fastapi-vs-flask/
'''


@app.get('/')
def hello_world():
    # qs = Logger.objects.all().first()
    return {'greet': f'Hello, World! '}

@sync_to_async
def insert_log(item):
    user = Logger(**item.__dict__)
    user.save()
    
 
class LogLine(BaseModel):
    message: str
    severity: str
    
    def get(self):
        return f'{self.message} {self.severity}' 


@app.post("/line/")
async def create_line(item: LogLine):
    
    await insert_log(item)
    return item
    
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
   
   
@app.post("/file/")
async def image(image: UploadFile = File(...), xml: UploadFile = File(...)):
    return {"filename": image.filename, 'xml': xml.filename}


some_file_path = "README.md"    
@app.get("/download/")
async def main():
    return FileResponse(some_file_path)


@app.get("/items/{item_id}/{page}")
async def read_item(item_id, page):

    return FileResponse(item_id)

import uvicorn

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
    
    
    
