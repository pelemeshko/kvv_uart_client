import time
import os


def create_log_file(file=None, prefix="", extension=".txt"):
    dir_name = "Logs"
    sub_dir_name = dir_name + "\\" + time.strftime("%Y_%m_%d", time.localtime()) + " Лог ADCS"
    try:
        os.makedirs(sub_dir_name)
    except (OSError, AttributeError) as error:
        pass
    try:
        if file:
            file.close()
    except (OSError, NameError, AttributeError) as error:
        pass
    file_name = sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                    time.localtime()) + prefix + " " + extension

    return file_name, sub_dir_name

def open_log_file(file_name):
    if file_name:
        try:
            file = open(file_name, 'a')
        except (OSError, NameError, AttributeError) as error:
            pass
    pass
    return file

def close_log_file(file):
    if file:
        try:
            file.close()
            #print('close')
        except (OSError, NameError, AttributeError) as error:
            pass
    pass
