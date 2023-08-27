report_dict = {}


def add_report(now_datetime_str: str, cmd_cod: int):
    if now_datetime_str not in report_dict:
        report_dict[now_datetime_str] = []
    report_dict[now_datetime_str].append(cmd_cod)
