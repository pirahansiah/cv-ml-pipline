import base64
from fastapi import FastAPI
from pydantic import BaseModel
from farshid import color_change


class Image(BaseModel):
    data: str


app = FastAPI()
@app.post("/process")
def process_image(img: Image):
    output = (color_change(img.data))
    return {"image": output}
