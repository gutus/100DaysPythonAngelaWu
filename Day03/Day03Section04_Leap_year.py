### LEAP YEAR - TAHUN KABISAT

year = int(input("Tahun  berapa yg ingin diperiksa?\t "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Tahun Kabisat")
    else:
      print("Bukan Tahun Kabisat")
  else:
    print("Tahun Kabisat")
else:
  print("Bukan Tahun Kabisat")
