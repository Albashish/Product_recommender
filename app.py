#import fastapi and uvicorn for building framework and using api to build requests.
from fastapi import Depends, FastAPI, Form, Request, Response, status
import uvicorn
import api 

app = FastAPI()
app.include_router(api.router, tags=["Search"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, log_level="info", reload=False)