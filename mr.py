from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# In-memory db
users_db = {}

class User(BaseModel):
    user: EmailStr
    assets: List[str] = []
    main: Optional[str] = None
class AssetInput(BaseModel):
    email: EmailStr
    asset_url: str

class EmailInput(BaseModel):
    email: EmailStr

class MainInput(BaseModel):
    email: EmailStr
    main_url: str

@app.get('/')
def home():
    return {'This is Home Page'}

@app.post("/create")
def create_user(email_input: EmailInput):
    email = email_input.email
    if email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[email] = User(user=email)
    return JSONResponse(content={"message": "User created successfully"})

@app.post("/update")
def update_assets(asset_input: AssetInput):
    email = asset_input.email
    asset_url = asset_input.asset_url
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[email].assets.append(asset_url)
    return JSONResponse(content={"message": "Asset added successfully"})

@app.post("/set")
def set_main(main_input: MainInput):
    email = main_input.email
    main_url = main_input.main_url
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[email].main = main_url
    return JSONResponse(content={"message": "Main URL set successfully"})

@app.get("/fetchMain")
def fetch_main(email_input: EmailInput):
    email = email_input.email
    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content={"main_url": users_db[email].main})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=int(os.environ.get('PORT', 8080)), host="127.0.0.1")
