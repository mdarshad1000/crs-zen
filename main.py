from fastapi import FastAPI
# from zenrows import ZenRowsClient  # Removed ZenRowsClient import
from dotenv import load_dotenv
import os
import json
from curl_cffi import requests  # Added import for curl_cffi

load_dotenv()

app = FastAPI()

@app.get("/scrape")
async def scrape():
    url = "https://crsreports.congress.gov/search/results?term=&r=59285836&orderBy=Date&navids=4294966212&pageNumber=5&"
    # Use curl_cffi's requests with impersonation instead of ZenRowsClient
    response = requests.get(url, impersonate="chrome110")
    json_response = json.loads(response.text)
    print(response.status_code)
    return {"x":json_response}


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=1234)