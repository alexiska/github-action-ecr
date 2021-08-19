from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_status_code():
   
        return "Failed to connect"

@app.get('/health')
async def get_status_code():
   
        return "200 OK"

