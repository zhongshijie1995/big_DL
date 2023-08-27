import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import List

import cv2
import loguru

from _comm import comm
from _logic import single_frame


class LocalCapture:
    def __init__(self):
        # 创建日志打印器
        self.log = loguru.logger
        # 单帧逻辑操作器
        self.sf = single_frame.SingleFrame()

    def realtime(self, feq: int, task_func_list: List[str], task_func_args_list: List[str]):
        if len(task_func_list) != len(task_func_args_list):
            # 退出函数
            self.log.info("任务列表和任务参数匹配失败")
            return
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
                    func = getattr(self.sf, task_func_list[i])
                    pool.submit(func, frame, task_func_args_list[i])
            # 如需警报，则附加警报色
            if now_datetime.strftime('%Y-%m-%d %H:%M:%S') in comm.report_dict:
                for cc in comm.report_dict[now_datetime.strftime('%Y-%m-%d %H:%M:%S')]:
                    frame = cv2.applyColorMap(frame, colormap=cc)
            # 实时打印视频帧
            cv2.imshow("实况回显", frame)
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
        self.log.info("退出")
        return
