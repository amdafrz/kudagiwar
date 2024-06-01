daftar_buku = {
  "Kita Bersama",
  "Sabi : Santai di Bali",
  "Evaluasi",
  "Padahal Kita Sama",
  "Kenapa Harus Setara?",
  "Dirimu Diriku Diriku Dirimu",
  "Secukupnya Saja",
  "Pernah Ada di Sampingku",
  "Nyata Namun Nyatanya Tiada",
  "Kenapa Hasur di Paksa?",
  "Palsu" : "00011",
  "Semuanya Sama Saja" : "00012",
  "Terhalang Jarak" : "00013",
  "Memotivasi" : "00014",
  "lebih Dekat" : "00015",
  "Setia" : "00016",
  "Dulu Sangat Indah" : "00017",
  "Menjadi Dewasa" : "00018",
  "Aku Sekarang Karena Aku Yang Dulu" : "00019",
  "Kamu Telah Berubah" : "00020"
} 

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
  nama_user = input("Masukan nama kamu: ")
  print("halo", nama_user + ", buku apa yang kamu cari hari ini ?")
  for judul,kode in zip(judul_buku, kode_buku):
      print(f"- Judul Buku : {judul.ljust(33)} - Kode Buku : {Kode}")
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
      
  
  
