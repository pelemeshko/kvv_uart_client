import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
from decimal import Decimal

import serial
import struct

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


def Bytes_to_NormBytes(data):
    buf = []
    for i in data:
        buf.append(hex(i))
    # print(buf)
    return buf


def Get_oscillogram():
    data_list = []
    points = []
    i = 0
    Get_oscillogram_com = [0x41, 0x01]
    ser.write(Get_oscillogram_com)
    #print('\nGet_oscillogram_com is sended,\t', 'time =', time.strftime("%Y_%m_%d %H-%M-%S "))
    output_data = ser.read(2048)
    #print(Bytes_to_NormBytes(output_data))
    while i < 2048:
        data_list.append(struct.unpack('<h', output_data[i:i + 2])[0])
        points.append(i)
        #print(i, Bytes_to_NormBytes(output_data)[i:i + 2], struct.unpack('<h', output_data[i:i + 2])[0])
        i = i + 2
    return data_list, points


def Plot(data_Y, data_X):
    plt.ion()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.plot(data_X, data_Y, color='black', linewidth=1)
    ax.grid(True)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_xlim([0, 2048])
    ax.set_ylim([0, 4200])
    #ax.scatter(data_X, data_Y, color='blue', marker='.')
    plt.pause(0.05)
    #plt.show()




def Plot2():
    x = np.linspace(0, 6 * np.pi, 100)
    y = np.sin(x)
    # You probably won't need this if you're embedding things in a tkinter plot...
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma

    for phase in np.linspace(0, 10 * np.pi, 500):
        line1.set_ydata(np.sin(x + phase))
        fig.canvas.draw()
        fig.canvas.flush_events()


while 1:
    data, Ppoints = Get_oscillogram()
    Plot(data, Ppoints)
    print(n)
    n = n + 1

ser.close()
