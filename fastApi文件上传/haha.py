import fastapi
import uvicorn
from fastapi import UploadFile, File, Body
from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")


@app.post("/api/upload_one")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    print(contents)
    return {"message": f"Successfuly uploaded {file.filename}"}


@app.post("/api/upload_two")
def upload_two(username: str, f: UploadFile = File(...)):
    """
    username默认是query
    :param username:
    :param f:
    :return:
    """
    print(username, f.filename)
    return 'ok'


@app.post("/api/upload_three")
async def upload_three(username: str = fastapi.Body('x'), f: UploadFile = File(...)):
    """
    username默认是query
    :param username:
    :param f:
    :return:
    """
    print(username, f.filename)
    content = await f.read()
    print(content)
    return 'ok'


@app.get("/api/haha")
def haha():
    return 'haha'


if __name__ == '__main__':
    uvicorn.run(app, port=1239)
