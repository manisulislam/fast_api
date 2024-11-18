from fastapi import FastAPI

app= FastAPI()

@app.get('/')
async def read_root():
    return {
        "message": "fast api server is ready"
    }