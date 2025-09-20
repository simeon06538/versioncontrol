import serial

ser = serial.Serial('COM3', 9600, timeout = 1)

print("scan barcode. press Ctrl+C to exit.")
try:
  while True:
    barcode = ser.readline().decode('utf-8').strip()
    if barcode:
      print("Scanned barcode")
except KeyboardInterrupt:
  print("Do not touch keyboard")
  ser.close()