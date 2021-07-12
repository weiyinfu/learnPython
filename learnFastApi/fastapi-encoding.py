from fastapi.encoders import jsonable_encoder
from datetime import datetime

print(jsonable_encoder({'x': datetime.now()}))
