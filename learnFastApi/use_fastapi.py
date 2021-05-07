import uvicorn
from fastapi import FastAPI, Request, Body, Response

app = FastAPI()


@app.post("/api/sum")
async def get_sum(req: Request):
    content = await req.json()
    a, b = content['a'], content['b']
    return a + b


@app.post("/api/sum2")
def get_sum2(a: int = Body(None), b: int = Body(None)):
    return int(a) + int(b)


@app.post("/api/add_later_see")
async def add_later_see(req: Request):
    content = await req.json()
    resp = Response("ok", headers={
        'Access-Control-Allow-Origin': "*"
    })
    return resp


def main():
    uvicorn.run(app)


def test():
    print(get_sum2(1, 2))


if __name__ == '__main__':
    main()
    # test()
