from fastapi import FastAPI
# from zenrows import ZenRowsClient  # Removed ZenRowsClient import
from dotenv import load_dotenv
import os
import json
from curl_cffi import requests

load_dotenv()

app = FastAPI()

@app.get("/scrape")
async def scrape():
    url = "https://crsreports.congress.gov/search/results?term=&r=59285836&orderBy=Date&navids=4294966212&pageNumber=5&"
    # Use curl_cffi's requests with impersonation instead of ZenRowsClient
    response = requests.get(url, impersonate="chrome124")
    # json_response = json.loads(response.text)
    x = response.status_code
    y = response.headers
    z = response.text
    return {"x":x, "y": y, "z": str(z)}


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=1234)