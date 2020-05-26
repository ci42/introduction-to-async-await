# requires the FastAPI and uvicorn packages:
# pip install fastapi
# pip install uvicorn
#
# start with: uvicorn fast-api:app --reload

import asyncio
import time

from fastapi import FastAPI

app = FastAPI()

@app.get("/async")
async def asynchronous():
    await asyncio.sleep(10)
    return "Hello world (asynchronous)!"

@app.get("/sync")
def synchronous():
    time.sleep(10)
    return "Hello world (synchronous)!"
