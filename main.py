from email import message
import matplotlib.pyplot as plt
import numpy as np
from arpaocalc import Ship, ARPA_calculations
from tkinter import *
from tkinter import ttk
from func import test


id = 419565453

a= [{'msg_type': 1, 'repeat': 0, 'mmsi': 419001261, 'status': '<NavigationStatus.Moored: 5>', 'turn': None, 'speed': 2.9, 'accuracy': False, 'lon': 73.05, 'lat': 19.085, 'course': 270, 'heading': 511, 'second': 1, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 49315},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419565453, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 3, 'accuracy': False, 'lon': 73.05928, 'lat': 19.029358, 'course': 270.0, 'heading': 511, 'second': 3, 'maneuver': 0, 'spare_1': b'\x00', 'raim': True, 'radio': 262144},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419565458, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 3, 'accuracy': False, 'lon': 73.05, 'lat': 18.829358, 'course': 90.0, 'heading': 511, 'second': 3, 'maneuver': 0, 'spare_1': b'\x00', 'raim': True, 'radio': 262144},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419565453, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 3, 'accuracy': False, 'lon': 73.05928, 'lat': 19.029358, 'course': 360.0, 'heading': 511, 'second': 4, 'maneuver': 0, 'spare_1': b'\x00', 'raim': True, 'radio': 262144},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419000482, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': 0.0, 'speed': 1, 'accuracy': False, 'lon': 72.915798, 'lat': 18.949165, 'course': 50.4, 'heading': 317, 'second': 4, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 49376},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419001261, 'status': '<NavigationStatus.Moored: 5>', 'turn': None, 'speed': 3.0, 'accuracy': False, 'lon': 72.88296, 'lat': 18.86736, 'course': 35.7, 'heading': 511, 'second': 3, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 114852},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419565453, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 2, 'accuracy': False, 'lon': 73.05928, 'lat': 19.029353, 'course': 360.0, 'heading': 511, 'second': 5, 'maneuver': 0, 'spare_1': b'\x00', 'raim': True, 'radio': 262144},
{'msg_type': 3, 'repeat': 0, 'mmsi': 419001261, 'status': '<NavigationStatus.Moored: 5>', 'turn': None, 'speed': 2.9, 'accuracy': False, 'lon': 72.88295, 'lat': 18.867372, 'course': 32.2, 'heading': 511, 'second': 4, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 0},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419001585, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': 0.0, 'speed': 1.0, 'accuracy': False, 'lon': 72.954813, 'lat': 18.972742, 'course': 26.4, 'heading': 33, 'second': 4, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 98547},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419565453, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 2, 'accuracy': False, 'lon': 73.05928, 'lat': 19.029353, 'course': 360.0, 'heading': 511, 'second': 6, 'maneuver': 0, 'spare_1': b'\x00', 'raim': True, 'radio': 262144},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419565453, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 1, 'accuracy': False, 'lon': 73.059287, 'lat': 19.029353, 'course': 360.0, 'heading': 511, 'second': 7, 'maneuver': 0, 'spare_1': b'\x00', 'raim': True, 'radio': 262144},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419001261, 'status': '<NavigationStatus.Moored: 5>', 'turn': None, 'speed': 2.8, 'accuracy': False, 'lon': 72.882935, 'lat': 18.867393, 'course': 31.0, 'heading': 511, 'second': 6, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 3508},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419767000, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': 0.0, 'speed': 7.6, 'accuracy': True, 'lon': 72.8956, 'lat': 18.935967, 'course': 238.0, 'heading': 240, 'second': 6, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 22072},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419575000, 'status': '<NavigationStatus.UnderWayUsingEngine: 0>', 'turn': None, 'speed': 1, 'accuracy': False, 'lon': 72.971545, 'lat': 19.015558, 'course':48.9, 'heading': 511, 'second': 6, 'maneuver': 0, 'spare_1': b'@', 'raim': False, 'radio': 49308},
{'msg_type': 1, 'repeat': 0, 'mmsi': 419956823, 'status': '<NavigationStatus.UnderWaySailing: 8>', 'turn': None, 'speed': 1, 'accuracy': False, 'lon': 73.248547, 'lat': 19.118387, 'course': 236.8, 'heading': 511, 'second': 11, 'maneuver': 0, 'spare_1': b'\x00', 'raim': False, 'radio': 254}]


# test(a)
win= Tk()
win.geometry("750x250")
Button(win, text= "Show Graph", command=lambda:  test(a,id_main=id)).pack(pady=20)
b1 = ttk.Button(win, text= "Change orientation +30", command=lambda: test(a,id,theta=30))
b1.place(x=200, y=100)
b2 = ttk.Button(win, text= "Change orientation +60", command=lambda: test(a,id,theta=60))
b2.place(x=200, y=150)  
b3 = ttk.Button(win, text= "Change orientation -30", command=lambda: test(a,id,theta =-30))
b3.place(x=450, y=100)
b4 = ttk.Button(win, text= "Change orientation -60", command=lambda: test(a,id,theta =-60))
b4.place(x=450, y=150)
win.mainloop()




    
