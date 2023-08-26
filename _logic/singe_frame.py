from typing import Any

import loguru

from _model.yolo_v5 import YoloV5Ctl


logger = loguru.logger

yolo_v5_ctl = YoloV5Ctl()
yolo_v5_ctl.init()


def say_hello(frame: Any, words: str):
    result = yolo_v5_ctl.detect(frame).pandas().xyxy[0]
    logger.info("任务【{}】，结果【{}】", words, result['name'].tolist())
    return
