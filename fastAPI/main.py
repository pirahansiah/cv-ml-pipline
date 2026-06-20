"""FastAPI endpoint for image color-space conversion."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from .farshid import color_change


class Image(BaseModel):
    data: str


app = FastAPI(title="CV ML Pipeline", version="2.0.0")


@app.post("/process")
def process_image(img: Image) -> dict[str, str]:
    output = color_change(img.data)
    return {"image": output}
