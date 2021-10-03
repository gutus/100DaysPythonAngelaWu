print("Selamat datang di rollercoaster Kami!")
tinggi = int(input("Berapakah tinggi anda dalam cm? "))
tiket = 0

if tinggi >= 120:
  print("Anda bisa menaiki rollercoaster!")
  usia = int(input("Berapa usia anda? "))
  if usia < 12:
    tiket = 5000
    print("Tiket anak-anak adalah Rp.5000.")
  elif usia <= 18:
    tiket = 7000
    print("Tiket anda adalah  Rp7000.")
  elif usia >= 45 and usia <= 55:
    print("Semuanya masih aman. Grati tiket untuk anda")
  else:
    tiket = 12000
    print("Tiket dewasa adalah Rp12000.")

  foto = input("Apakah anda ingin berfoto juga? Ya atau Tidak. ")
  if foto == "Ya":
    tiket += 3000

  print(f"Total yang harus anda bayar adalah  Rp{tiket}")

else:
  print("Maaf, tinggi anda masih belum cukup, \nperlatan safety kami  sudah disetel untuk tinggi badan minimal tertentu.")
