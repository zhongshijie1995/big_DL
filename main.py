from _tool import local_capture

if __name__ == '__main__':
    task_func_list = [
        # 'person_with_cell_phone',
        # 'no_person',
        'person_without_cell_phone',
    ]
    task_func_args_list = [
        # '携手机人员',
        # '无人在值',
        '有人在值且不可携手机',
    ]
    lc = local_capture.LocalCapture()
    lc.realtime(1, task_func_list, task_func_args_list)
