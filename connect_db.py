from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_status_code():
   
        return "Failed to connect"

