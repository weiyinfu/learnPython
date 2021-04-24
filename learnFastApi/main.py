from fastapi import FastAPI

app = FastAPI()

subapi = FastAPI()


@subapi.get("/")
async def root():
    return {"message": "Hello World"}


another = FastAPI()


@another.get("/baga")
def baga():
    return {'baga'}


app.mount("/haha", subapi)
app.mount("/hahax", another)
