import time
import socket
import csv
import datetime
import win32api

# Arduino connection setting
HOST = 'arduino.local'
PORT = 8080

with open('output.csv', 'w', newline='') as f:

    # CSV file for data logging
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Timestamp', 'Sensor1', 'Sensor2'])

    # Start main process
    while True:
        print('-----------------------')

        # Get the data from the Arduino Yun
        try:
            # Try connecting to Arduino and get data
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Connect to arduino
                s.connect((HOST, PORT))
                # Receive data from arduino
                data_arduino = str(s.recv(1024), encoding='utf-8')
                # Split the data into sensor 1 and sensor2
                value1, value2 = data_arduino.split('/')
                # Check if water head is high enough
                if value1 == '1' or value2 == '0':
                    # If water head is too high, display alert window
                    win32api.MessageBox(0x10, 'Water head too high!', 'Alert!')
                # Print log
                print('Arduino Data :', data_arduino)

        except:
            # If connection is not established, print error message and try again after 2 seconds.
            print('Could not connect to Arduino. Try again after 2 seconds.')
            time.sleep(2)
            continue

        # Concatenate data and write it to csv file
        csv_writer.writerow([datetime.datetime.now(), value1, value2])

        # Flush data
        f.flush()

        # Wait for 2 seconds
        time.sleep(1)
