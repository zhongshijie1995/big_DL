from _tool import local_capture
from _logic import singe_frame

if __name__ == '__main__':
    task_func_list = [singe_frame.say_hello, ]
    task_func_args_list = ["显示目标", ]
    local_capture.realtime(3, task_func_list, task_func_args_list)
