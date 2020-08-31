import serial
import time
import sys

if __name__ == "__main__":
    import serial.tools.list_ports

    print('Search...')
    ports = serial.tools.list_ports.comports(include_links=False)
    for port in ports:
        print('Find port ' + port.device)

    ser = serial.Serial(port=port.device, baudrate=115200, timeout=0.5)
    # ser.open()

    date = sys.argv[1]  # change the date to the date of today

    ser.write(b'svc_app format_id 7\r')  #换去HDR模式

    time.sleep(1)
    ser.write(b'svc_rawcap cfg 4 7\r')  #//capture camera 1 raw data
    time.sleep(1)

    image_nums = 10000

    for index in range(image_nums):
        index = "%06d" % index
        command1 = "svc_rawcap cfg_itn 1 c:\\" + date + "_f" + index + "_vin2.txt\r"
        command2 = "svc_rawcap cap 2 c:\\" + date + "_f" + index + "_vin2.raw  c:\\" + date + "_f" + index + "_vin2_hds.raw\r"
        ser.write(command1.encode('ascii'))
        time.sleep(1)
        ser.write(command2.encode('ascii'))
        time.sleep(3)

        result = ser.readlines()  # .decode('utf-8')
        for line in result:
            print(line.decode())  # if system language is chinese, use 'utf-8' decode

    ser.close()
