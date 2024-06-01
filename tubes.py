judul_buku = [
  "Kita Bersama",
  "Sabi : Santai di Bali",
  "Evaluasi",
  "Padahal Kita Sama",
  "Kenapa Harus Setara?",
  "Dirimu Diriku Diriku Dirimu",
  "Secukupnya Saja",
  "Pernah Ada di Sampingku",
  "Nyata Namun Nyatanya Tiada",
  "Kenapa Harus di Paksa?",
  "Palsu",
  "Semuanya Sama Saja",
  "Terhalang Jarak",
  "Memotivasi",
  "Lebih Dekat",
  "Setia",
  "Dulu Sangat Indah",
  "Menjadi Dewasa",
  "Aku Sekarang Karena Aku Yang Dulu",
  "Kamu Telah Berubah"
]

kode_buku = [
  "00001",
  "00002",
  "00003",
  "00004",
  "00005",
  "00006",
  "00007",
  "00008",
  "00009",
  "00010",
  "00011", 
  "00012", 
  "00013", 
  "00014", 
  "00015", 
  "00016", 
  "00017", 
  "00018", 
  "00019", 
  "00020", 
]

def cari_buku():
    print("============ Selamat Datang di Perpustakaan Kuda Giwar =============")
    nama_user = input("Masukkan nama kamu: ")
    print("====================================================================")
    print("Hallo", nama_user + ", buku apa yang kamu cari hari ini ?")
    print("====================================================================")
  for judul,kode in zip(judul_buku, kode_buku):
      print(f"- Judul Buku : {judul.ljust(33)} - Kode Buku : {kode}")
  while True:
      print("====================================================================")
      input_user = input("Ketik Judul atau Kode Buku disini: ")
      print("====================================================================")
      if input_user in judul_buku:
        kode = kode_buku[judul_buku.index(input_user)]
        print("Judul Buku yang kamu cari:", input_user + ", dengan Kode :", kode)
        print("====================================================================")
        break
      elif input_user in kode_buku:
        judul = judul_buku[kode_buku.index(input_user)]
        print("Judul Buku yang kamu cari:", judul + ", dengan Kode:", input_user)
        print("====================================================================")
        break
      else:
        print("Tidak ada hasil, Ketik nama atau kode buku dengan benar.")
cari_buku()
      
  
  
