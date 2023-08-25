from typing import Dict

from fastapi import FastAPI

from _model import yolo_v5


# 初始化Web服务APP
app = FastAPI()

# 初始化模型
yolo_v5_ctl = yolo_v5.YoloV5Ctl()
yolo_v5_ctl.init()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/yolo_v5_demo")
async def yolo_v5_demo(req: Dict):
    result_str = yolo_v5_ctl.detect_by_url(req.get("imgUrl"))
    return {"message": result_str}
