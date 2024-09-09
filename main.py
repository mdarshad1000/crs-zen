from fastapi import FastAPI
from dotenv import load_dotenv
from zenrows import ZenRowsClient
import os
import json

load_dotenv()


app = FastAPI()
client = ZenRowsClient(os.getenv("ZENROWS_API_KEY"))

@app.get("/fetch-data")
async def fetch_data():

    url = "https://crsreports.congress.gov/search/results?term=&r=55600006&orderBy=Date&navids=4294966212&"

    response = client.get(url)
    json_data = json.loads(response.text)
    print(response.status_code)
    return json_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)