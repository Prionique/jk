from fastapi import *

app = FastAPI()

@app.get("/")
def main(user):
    return user[::-1]

