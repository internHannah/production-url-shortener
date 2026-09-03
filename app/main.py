from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random
import string
from pydantic import BaseModel

class URL(BaseModel):
    original_url: str
    short_url: str
    code: str

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

app = FastAPI()

url_store = {}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/urls")   
async def create_url(url: str):
    code = generate_code() 
    url_store[code] = URL(original_url=url, short_url=f"http://localhost:8000/{code}", code=code)
    return url_store[code]

@app.get("/{code}")
def redirect_to_url(code: str):
    if code not in url_store:
        raise HTTPException(status_code=404, detail="Unknown code")
    return RedirectResponse(status_code=302, url=url_store[code].original_url)
