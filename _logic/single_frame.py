import datetime
from typing import Any

import cv2
import loguru

from _comm import comm
from _model.yolo_v5 import YoloV5Ctl


class SingleFrame:
    def __init__(self):
        # 创建日志打印器
        self.log = loguru.logger
        # 初始化YOLO_V5通用模型
        self.yolo_v5_ctl = YoloV5Ctl()
        self.yolo_v5_ctl.init()

    def person_with_cell_phone(self, frame: Any, words: str):
        result = self.yolo_v5_ctl.detect(frame).pandas().xyxy[0]
        target_type_list = result['name'].tolist()
        self.log.info("任务【{}】，结果【{}】", words, target_type_list)
        now_datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if 'person' in target_type_list and 'cell phone' in target_type_list:
            comm.add_report(now_datetime_str, cv2.COLORMAP_HOT)
        return

    def no_person(self, frame: Any, words: str):
        result = self.yolo_v5_ctl.detect(frame).pandas().xyxy[0]
        target_type_list = result['name'].tolist()
        self.log.info("任务【{}】，结果【{}】", words, target_type_list)
        now_datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if 'person' not in target_type_list:
            comm.add_report(now_datetime_str, cv2.COLORMAP_COOL)
        return

    def person_without_cell_phone(self, frame: Any, words: str):
        result = self.yolo_v5_ctl.detect(frame).pandas().xyxy[0]
        target_type_list = result['name'].tolist()
        self.log.info('任务【{}】-检出对象：{}', words, target_type_list)
        now_datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if 'person' in target_type_list and 'cell phone' in target_type_list:
            comm.add_report(now_datetime_str, cv2.COLORMAP_HOT)
        if 'person' not in target_type_list:
            comm.add_report(now_datetime_str, cv2.COLORMAP_COOL)
        return
