from PyPDF2 import PdfWriter, PdfReader
  
# buat objek pdf writer
out = PdfWriter()
# buka file pdf asli 
file = PdfReader("file_pdf.pdf")
# identifikasi total halaman file
num = file.numPages
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for page in file.pages:
    # tambahkan halaman ke objek pdf writer
    out.add_page(page)
    
# masukkan password enkripsi 
password = "12345"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("Encrypted_pdf.pdf", "wb") as f:
    # simpan pdf 
    out.write(f)