import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
from decimal import Decimal

import serial
import struct

import numpy.fft as fft

import log_file

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'
ser.open()
print(ser.name + ' is opened...')
ser.flushOutput()  # очистка выходного буфера
ser.flushInput()  # очистка входного буфера
ser.reset_output_buffer()
ser.reset_input_buffer()
n = 0

fig = plt.figure()

#
# file_handle_1, log_dir_1 = log_file.create_log_file1(prefix="kvv_log", extension=".txt")
# file_1 = log_file.open_log_file_1(file_handle_1)
# file_1.write("Time\tCommand Name\tCommand\tAnswer\n")
# log_file.close_log_file_1(file_handle_1)



def input_file_path():
    """Enter number of the selected channel; """
    channel = 0
    input_str1 = input('Enter number of the selected channel [1-14]:', )
    try:
        channel = input_str1
        print('Selected channel is', channel)
    except IndexError:
        print('Error!')
    return channel


def Bytes_to_NormBytes(data):
    buf = []
    for i in data:
        buf.append(hex(i))
    # print(buf)
    return buf


def Get_oscillogram(channel):
    data_list = []
    points = []
    i = 0
    Get_oscillogram_com = [0x41, int(channel)]
    ser.write(Get_oscillogram_com)
    #print('\nGet_oscillogram_com is sended,\t', 'time =', time.strftime("%Y_%m_%d %H-%M-%S "))
    output_data = ser.read(2048)
    #print(Bytes_to_NormBytes(output_data))
    while i < 2048:
        data_list.append(struct.unpack('<h', output_data[i:i + 2])[0])
        """points in ms; """
        points.append(i*81.92/2048)
        #print(i, Bytes_to_NormBytes(output_data)[i:i + 2], struct.unpack('<h', output_data[i:i + 2])[0])
        i = i + 2
    return data_list, points


def Plot(data_Y, data_X):
    plt.ion()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.plot(data_X, data_Y, color='black', linewidth=1)
    ax.grid(True)
    ax.set_xlabel('time, ms')
    ax.set_ylabel('y-axis')
    ax.set_xlim([0, 81.92])
    ax.set_ylim([0, 4200])
    #ax.scatter(data_X, data_Y, color='blue', marker='.')
    plt.pause(0.05)
    #plt.show()


Ch = input_file_path()
while 1:
    data, Ppoints = Get_oscillogram(Ch)
    Plot(data, Ppoints)
    print(n, 'freq is')
    n = n + 1

ser.close()
