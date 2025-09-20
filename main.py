print("Ready to scan barcodes. Press CTRL+C to stop")

try:
  while True:
    barcode = input("Scan a barcode: ")
    if barcode:
      print("Scannerd barcode: " + barcode)
except KeyboardInterrupt:
  print("Stopped scanning ")
