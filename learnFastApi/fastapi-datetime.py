import json
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import bes

app = FastAPI()


@app.get("/")
def get():
    ans = {
        'x': datetime.now(),
    }
    print(json.dumps(ans))
    return ans


uvicorn.run(app)
