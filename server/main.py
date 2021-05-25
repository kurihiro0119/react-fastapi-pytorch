from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/kuri/")
def read_root():
  return {"Kurihara": "Hironari"}

@app.post("/")
def read_root():
  return {"Hello": "Post"}