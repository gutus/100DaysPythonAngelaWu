# TIP CALCULATOR
# Untuk menghitung tagihan per orang beserta tip nya
print("Selamat datang, mari kita hitung tagihan tiap orang.")
tagihan = int(input("Berapa besaranya tagihan bill total? "))
tip = int(input("Berapa besaran tip untuk pelayan, 10, 12 atau 15% ? "))
orang = int(input("Berapa banyaknya orang yg akan ditagih? "))

tip_persentase = tip/100
besaran_tip = tip_persentase * tagihan
total_tagihan_semua = tagihan + besaran_tip
tagihan_per_orang = total_tagihan_semua / orang
tagihan_final = round(tagihan_per_orang, 0)

print(f"Besar tagihan awal {tagihan}")
print(f"Besaran tip yg dipilih {tip}% dengan besaran {besaran_tip}")
print(
    f"Total tagihan {tagihan} + tip {besaran_tip} = {total_tagihan_semua}")
print(
    f"Total tagihan semua {total_tagihan_semua} / {orang} = {tagihan_per_orang}")
print(f"Jadi tiap orang membayar sebesar Rp {tagihan_final}")
