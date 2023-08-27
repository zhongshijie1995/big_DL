import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import List, Callable

import cv2
import loguru

from _model import yolo_v5
from _comm import comm

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
    last_task_datetime = None
    # 循环捕获
    while True:
        # 获取当前时间
        now_datetime = datetime.datetime.now()
        # 提取视频帧
        ret, frame = cap.read()
        if now_datetime.second % feq == 0 and last_task_datetime != now_datetime.second:
            last_task_datetime = now_datetime.second
            for i in range(len(task_func_list)):
                pool.submit(task_func_list[i], frame, task_func_args_list[i])
        # 如需警报，则附加警报色
        if comm.report_datetime == now_datetime.strftime('%Y-%m-%d %H:%M:%S'):
            frame = cv2.applyColorMap(frame, colormap=cv2.COLORMAP_HOT)
        # 实时打印视频帧
        cv2.imshow("实况", frame)
        # 提取结束指令
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # 停止线程池
    pool.shutdown(wait=False)
    # 结束捕获器
    cap.release()
    # 销毁窗口
    cv2.destroyAllWindows()
    # 退出函数
    logger.info("中止，退出函数")
    return
