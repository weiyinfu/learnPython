fastapi是什么？
* 一个python web框架，对标flask和django
* 一个异步框架，对标js express和java中的vertx
* 一个api定义语言，使用python来书写idl
* 一个参数自动绑定的web框架，对标springboot。

优点：
* 性能超高：媲美golang
* 测试简单：对于接口的测试，直接调用函数进行测试
* 写法简单：不用绑定参数
* 自动生成可视化API文档

# 快速开始
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
fastapi不像flask可以直接app.run(),需要使用命令执行：`uvicorn main:app --reload`。然后访问以下链接查看效果：

* http://127.0.0.1:8000/
* http://127.0.0.1:8000/redoc
* http://127.0.0.1:8000/docs

# 路径参数
```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
    
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```
    
# query中的参数
https://fastapi.tiangolo.com/zh/tutorial/query-params/

超级灵活的bool类型：on，off，yes，no，1，0，true，false应有尽有

# post请求使用pydantic
post请求使用pydantic
```python
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
```

函数参数将依次按如下规则进行识别：

如果在路径中也声明了该参数，它将被用作路径参数。
如果参数属于单一类型（比如 int、float、str、bool 等）它将被解释为查询参数。
如果参数的类型被声明为一个 Pydantic 模型，它将被解释为请求体。

# 使用Query明确声明参数来源
```python
from fastapi import FastAPI, Query
from typing import Optional
app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    ...

```
声明为必选参数  
`async def read_items(q: str = Query(..., min_length=3))`

数组形式的query
`async def read_items(q: Optional[List[str]] = Query(None)):`

fastapi是一个api声明工具，相当于ferry，相当于swagger，它可以用于定义api接口。

各种花式Query：
```plain
Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
    
Query(None, alias="item-query"))

Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )

```
# 路径参数
对于路径参数，同样可以执行校验。
```plain
Path(..., title="The ID of the item to get"),
Path(..., title="The ID of the item to get", gt=0, le=1000)
```
使用`*`来强制要求使用参数名
```plain
read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):

```

补充一下typing的知识：`Union[MyClass,None]=Optional[MyClass]`
```plain
from typing import List
my_list: List[str]
```

在参数中如果有多个pydantic结构体，相当于直接解开一层`item: Item, user: User`

使用body指定请求体中的单个值。单个值如果不指明body，则默认是query中的参数。

```plain
update_item(
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
```

嵌入请求体，即便只有一个pydantic结构体，依旧下钻一层，极其符合人体工学。
```plain
item: Item = Body(..., embed=True)
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}

```


请求体中也可以进行各种声明，Field字段来自于pydantic而不是fastapi
```plain
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None

```
    
使用Set类型
```plain
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
```

pydantic结构体也支持嵌套。

纯列表
```plain
class Image(BaseModel):
    url: HttpUrl
    name: str
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images
# 简单类型+Dict也能组成请求体。
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

```  
# pydantic进阶
指定example，指定Config schema_extra
```plain
class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

```

使用body的时候指定额外参数
```plain
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results

```
    
Cookie、header也是一样的香甜。
```plain
@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}
@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}
```

header中经常使用连字符，默认把连字符转换成下划线，可以关闭它。注意：header不区分大小写。  
```plain
async def read_items(
    strange_header: Optional[str] = Header(None, convert_underscores=False)
):
# 重复headers使用数组即可。  
def read_items(x_token: Optional[List[str]] = Header(None)):

```


# 响应模型：返回值依旧可以使用pydantic
如：`@app.post("/items/", response_model=Item)`

你的响应模型可以具有默认值，例如：

响应可以有默认值，也可以避免返回那些为空的字段，减少网络带宽的浪费。 
```plain
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
    
    
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
```

    
表单也是一样的呀。
```python
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

```
    
文件也没区别
```python
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

# 使用静态文件
需要安装依赖：`pip install aiofiles`
```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
```

# 在代码中运行
```python
import unicorn
uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
```
