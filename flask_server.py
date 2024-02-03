# main.py
from fastapi import FastAPI, UploadFile, HTTPException
# import cv2
# from ultralytics import YOLO

# import numpy as np
app = FastAPI()
# from PIL import Image
# from io import BytesIO




@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/predict/")
async def predict_image(data):
    print(data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)