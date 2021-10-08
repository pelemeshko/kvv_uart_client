import time
import os


def create_log_file1(file=None, prefix="", extension=".txt"):
    dir_name = "Logs"
    sub_dir_name = dir_name + "\\" + time.strftime("%Y_%m_%d", time.localtime()) + " Лог СКЭ"
    try:
        os.makedirs(sub_dir_name)
    except (OSError, AttributeError) as error:
        pass
    try:
        if file:
            file.close()
    except (OSError, NameError, AttributeError) as error:
        pass
    file_name_1 = sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                    time.localtime()) + prefix + " СКЭ" + extension

    return file_name_1, sub_dir_name

def create_log_file2(file=None, prefix="", extension=".txt"):
    dir_name = "Logs"
    sub_dir_name = dir_name + "\\" + time.strftime("%Y_%m_%d", time.localtime()) + " Лог СКЭ"
    try:
        os.makedirs(sub_dir_name)
    except (OSError, AttributeError) as error:
        pass
    try:
        if file:
            file.close()
    except (OSError, NameError, AttributeError) as error:
        pass
    file_name_2 = sub_dir_name + "\\" + time.strftime("%Y_%m_%d %H-%M-%S ",
                                                    time.localtime()) + prefix + " СКЭ" + extension

    return file_name_2, sub_dir_name

def open_log_file_1(file_name_1):
    if file_name_1:
        try:
            file_1 = open(file_name_1, 'a')
        except (OSError, NameError, AttributeError) as error:
            pass
    pass
    return file_1

def close_log_file_1(file_1):
    if file_1:
        try:
            file_1.close()
            print('close')
        except (OSError, NameError, AttributeError) as error:
            pass
    pass

def open_log_file_2(file_name_2):
    if file_name_2:
        try:
            file_2 = open(file_name_2, 'a')
        except (OSError, NameError, AttributeError) as error:
            pass
    pass
    return file_2

def close_log_file_2(file_2):
    if file_2:
        try:
            file_2.close()
            #print('close')
        except (OSError, NameError, AttributeError) as error:
            pass
    pass