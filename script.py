import os 
import requests 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPEN_API_KEY")


# Gemini API Endpoint (using gemini-2.5-flash)
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"

headers={
    "Content-Type":"application/json"
}

payload={
    "contents":[{"parts":[{"text":"What is JSONFormat"}]}]
}

response = requests.post(url,headers=headers,json=payload)

#parsing json

if response.status_code==200:
    data= response.json()
    print("AI Answers",data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print (f"Error {response.status_code}: {response.text}")