from fastapi import FastAPI,Request,Depends
from fastapi.templating import Jinja2Templates
import models
from sqlalchemy.orm import Session
from database import SessionLocal,engine
from pydantic import BaseModel

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

templates = Jinja2Templates(directory = 'templates')
#n = int(input('enter the value : '))

class StockRequest(BaseModel):
    symbol : str
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
def home(request : Request):
    return templates.TemplateResponse('dashboard.html',{
        'request': request
    })

@app.get('/name/{names}')
def item(names :str,q:str = None):
    return {'name':names,'query':q}

@app.post('/stock')
def home(stock_request:StockRequest,db:Session = Depends(get_db)):
    return {
       'code':'success',
       'message':'stock created'
    }