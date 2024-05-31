daftar_buku = {
  "Kita Bersama" : "00001",
  "Sabi : Santai di Bali" :"00002",
  "Evaluasi" :"00003",
  "Padahal Kita Sama" :"00004",
  "Kenapa Harus Setara?" :"00005",
  "Dirimu Diriku Diriku Dirimu" :"00006",
  "Secukupnya Saja" :"00007",
  "Pernah Ada di Sampingku" :"00008",
  "Nyata Namun Nyatanya Tiada" :"00009",
  "Kenapa Hasur di Paksa?" :"00010",
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

def cari_buku():
  nama_user = input("Masukan nama kamu: ")
  print("halo", nama_user + ", buku apa yang kamu cari hari ini ?")
  for nama_buku, kode in daftar_buku.items():
       print(f"- Judul Buku : {nama_buku.ljust(33)} - Kode Buku : {kode}")
  while True : 
    input_user = input("Ketik judul atau kode buku disini : ")
    if input_user in daftar_buku:
       print("Juduk Buku yang kamu cari:", input_user + ", dengan Kode:", daftar_buku[inout_user])
       break
    elif input_user in daftar_buku.values():
       nama_buku = [nama for nama, kode in daftar_buku.items() if kode == input_user[0]
       print("Judul buku yang kamu cari:", nama_buku + ", dengan Kode:", input_user)
       break
    else:
       print("Tidak ada hasil!, ketik nama buku atau kode buku dengan benar.")
cari_buku()
      
  
  
