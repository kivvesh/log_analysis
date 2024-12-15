import os
from pprint import pprint

from settings import ROOT_DIR, PATH
from core.work_os import is_dir_or_file, get_all_files_from_dir
from core.work_log import get_log, get_top_ips, get_top_longest, get_total_stat
from core.dump import  dump_allure

# get_log(os.path.join(ROOT_DIR,'data','access.log'))


def main():
    if PATH:
        is_dir = is_dir_or_file(PATH)
        if is_dir:
            list_files = get_all_files_from_dir(PATH)
        else:
            list_files = [PATH]
    else:
        list_files = get_all_files_from_dir(os.path.join(ROOT_DIR,'data'))

    all_logs = []
    for file in list_files:
        all_logs += get_log(file)

    get_total_stat(all_logs)
    data = {
        'top_ips': get_top_ips(all_logs),
        'top_longest': get_top_longest(all_logs),
        'total_stat': get_total_stat(all_logs),
        'total_requests': len(all_logs)
    }
    pprint(data)
    dump_allure(data)




if __name__ == '__main__':
    main()
