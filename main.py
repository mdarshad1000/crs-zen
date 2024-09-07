from fastapi import FastAPI
from zenrows import ZenRowsClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()  # Create a FastAPI instance

client = ZenRowsClient(os.getenv("ZENROWS_API_KEY"))

@app.get("/scrape")
async def scrape():
    url = "https://crsreports.congress.gov/search/results?term=&r=59285836&orderBy=Date&navids=4294966212&pageNumber=5&"
    response = client.get(url)
    res = {"x": str(response)}
    return res

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=1234)