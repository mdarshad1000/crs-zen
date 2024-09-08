from fastapi import FastAPI
from curl_cffi import requests


app = FastAPI()

@app.get("/fetch-data")
async def fetch_data():
    cookies = {
        'AMCVS_0D15148954E6C5100A4C98BC%40AdobeOrg': '1',
        's_ecid': 'MCMID%7C81710461424735814132251758168733180272',
        's_cc': 'true',
        'ASP.NET_SessionId': 'ciimk4xwu5rhyhbebipfcmi2',
        '__cfruid': 'a9722f8935700119f2bde35a08cef557a10e0fe0-1725492540',
        's_sq': '%5B%5BB%5D%5D',
        '__cf_bm': 'xhFhG5ywJ_78TDjmyt.XfyJS.5qwt7qip6zjgzWRMg8-1725814193-1.0.1.1-us5XUMq8kR.q40rkijeK5aCXzY.T2d.zp_vSL9xPYQzSFe1sQnQvzrHtTMGLgu1lyHi5.i5fGisd6lSOBFX4NA',
        'AMCV_0D15148954E6C5100A4C98BC%40AdobeOrg': '179643557%7CMCIDTS%7C19974%7CMCMID%7C81710461424735814132251758168733180272%7CMCAAMLH-1726418996%7C12%7CMCAAMB-1726418996%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1725821396s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ht;q=0.7',
        # 'cookie': 'AMCVS_0D15148954E6C5100A4C98BC%40AdobeOrg=1; s_ecid=MCMID%7C81710461424735814132251758168733180272; s_cc=true; ASP.NET_SessionId=ciimk4xwu5rhyhbebipfcmi2; __cfruid=a9722f8935700119f2bde35a08cef557a10e0fe0-1725492540; s_sq=%5B%5BB%5D%5D; __cf_bm=xhFhG5ywJ_78TDjmyt.XfyJS.5qwt7qip6zjgzWRMg8-1725814193-1.0.1.1-us5XUMq8kR.q40rkijeK5aCXzY.T2d.zp_vSL9xPYQzSFe1sQnQvzrHtTMGLgu1lyHi5.i5fGisd6lSOBFX4NA; AMCV_0D15148954E6C5100A4C98BC%40AdobeOrg=179643557%7CMCIDTS%7C19974%7CMCMID%7C81710461424735814132251758168733180272%7CMCAAMLH-1726418996%7C12%7CMCAAMB-1726418996%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1725821396s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
        'priority': 'u=1, i',
        'referer': 'https://crsreports.congress.gov/search/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://crsreports.congress.gov/search/results?term=&r=59414168&orderBy=Date&navids=4294966212&pageNumber=3&',
        cookies=cookies,
        headers=headers,
        impersonate='chrome120'
    )

    print(response.status_code)
    return response.text

if __name__ == '__main__':
    import uvicorn 
    
    uvicorn.run(app, host="0.0.0.0", port=1234)