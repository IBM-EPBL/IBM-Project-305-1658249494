#!/usr/bin/python
import struct, array, time, io, fcntl

I2C_SLAVE=0x0703

# find with  sudo i2cdetect -y 1
HDC1008_ADDR = 0x40

bus=1
fr = io.open("/dev/i2c-"+str(bus), "rb", buffering=0)
fw = io.open("/dev/i2c-"+str(bus), "wb", buffering=0)

# set device address
fcntl.ioctl(fr, I2C_SLAVE, HDC1008_ADDR)
fcntl.ioctl(fw, I2C_SLAVE, HDC1008_ADDR)
time.sleep(0.015) #15ms startup time

s = [0x02,0x02,0x00]
s2 = bytearray( s )
fw.write( s2 ) #sending config register bytes
time.sleep(0.015)               # From the data sheet

s = [0x00] # temp
s2 = bytearray( s )
fw.write( s2 )
time.sleep(0.0625)              # From the data sheet

data = fr.read(2) #read 2 byte temperature data
buf = array.array('B', data)
print ( "Temp: %f" % (  ((((buf[0]<<8) + (buf[1]))/65536.0)*165.0 ) - 40.0  )   )

time.sleep(0.015)               # From the data sheet

s = [0x01] # hum
s2 = bytearray( s )
fw.write( s2 )
time.sleep(0.0625)              # From the data sheet

data = fr.read(2) #read 2 byte temperature data
buf = array.array('B', data)
print ( "Humidity: %f" % (  ((((buf[0]<<8) + (buf[1]))/65536.0)*100.0 ) ) )
