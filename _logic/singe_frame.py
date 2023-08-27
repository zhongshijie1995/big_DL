import datetime
from typing import Any

import loguru

from _model.yolo_v5 import YoloV5Ctl
from _tool import comm


logger = loguru.logger

yolo_v5_ctl = YoloV5Ctl()
yolo_v5_ctl.init()


def say_hello(frame: Any, words: str):
    result = yolo_v5_ctl.detect(frame).pandas().xyxy[0]
    target_type_list = result['name'].tolist()
    logger.info("任务【{}】，结果【{}】", words, target_type_list)
    if 'person' in target_type_list and 'cell phone' in target_type_list:
        comm.report_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return
