import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable

import cv2
import loguru

from _model import yolo_v5


logger = loguru.logger


def realtime(feq: int, task_func_list: List[Callable], task_func_args_list: List[str]):
    if len(task_func_list) != len(task_func_args_list):
        # 退出函数
        logger.info("任务列表和任务参数匹配失败")
        return
    # 初始化模型
    yolo_v5_ctl = yolo_v5.YoloV5Ctl()
    yolo_v5_ctl.init()
    # 准备线程池
    pool = ThreadPoolExecutor(max_workers=5)
    # 准备捕获器
    cap = cv2.VideoCapture(1)
    # 时间冲撞器
    last_task_second = 61
    # 循环捕获
    while True:
        # 提取视频帧
        ret, frame = cap.read()
        # 实时打印视频帧
        cv2.imshow("video", frame)
        now_second = datetime.datetime.now().second
        if now_second % feq == 0 and last_task_second != now_second:
            last_task_second = now_second
            for i in range(len(task_func_list)):
                pool.submit(task_func_list[i], frame, task_func_args_list[i])
        # 提取结束指令
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    pool.shutdown(wait=False)
    # 结束捕获器
    cap.release()
    # 销毁窗口
    cv2.destroyAllWindows()
    # 退出函数
    logger.info("中止，退出函数")
    return
