from _tool import local_capture
from _logic import singe_frame

if __name__ == '__main__':
    task_func_list = [singe_frame.person_with_cell_phone, ]
    task_func_args_list = ["携手机人员", ]
    local_capture.realtime(1, task_func_list, task_func_args_list)
