from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
#from Scrapper import run_scrapper  
#from fastapi_utils.tasks import repeat_every

app = FastAPI()
origins = ['http://localhost:3000','http://localhost:4567']
names = ['misli','888sport','betway','nesine','unibet','bet10','marathon','tuttur']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from database import (
    fetch_all_teams,
    fetch_all_odds,
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/teams")
async def get_teams():
    responses = []
    for name in names:
        response = await fetch_all_teams(name)
        response = (name, response)
        responses.append(response)
    return responses

@app.get("/api/odds")
async def get_odds():
    responses = []
    for name in names:
        response = await fetch_all_odds(name)
        response = (name, response)
        responses.append(response)
    return responses

@app.get("/api/teams/{id}")
async def get_team(id):
    response = await fetch_all_teams(id)
    return response

@app.get("/api/odds/{id}")
async def get_odd(id):
    response = await fetch_all_odds(id)
    return response

@app.get("/api/max")
def get_max_values():
    from AnomaliTahmini import max_matrix
    return max_matrix

@app.get("/api/anomalies")
def get_anomalies():
    from AnomaliTahmini import anomaly_matrix
    return anomaly_matrix

#@app.on_event("startup")
#@repeat_every(seconds=60 * 20,wait_first=True)
#def startup_event():
#        run_scrapper()
#        print("Web Scrapping Done")   


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)