# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:54:37 2022

@author: tamas.jaszi
"""

import serial
import asyncio

ser = serial.Serial(
    port='COM7',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')

async def read():
    while True:
        out = ''
        while (ser.in_waiting > 0):
            out += str(ser.read(1), 'utf-8')    
        if out != '':
                print (">>" + out)
                out = ''
        await asyncio.sleep(0)

async def write():
    while True:
        inp = input(">> ")
        if inp == 'exit':
            ser.close()
            exit()
        else:
            ser.write(inp.encode('utf-8')) # + '\r\n')
        await asyncio.sleep(0)

print("luk")
asyncio.gather(read(),write())
asyncio.get_event_loop().run_forever()

print ("pina")