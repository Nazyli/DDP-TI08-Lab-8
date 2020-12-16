# Nama: Evry Nazyli Ciptanto
# NIM: 0110220045
# Kelas: Teknik Informatika 08 Weekend

def hitung_kemunculan(s):
  # Tulis kode fungsi hitung_kemunculan() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # membuat dictionary kosong
  x = {}
  # melakukan perulangan sebanyak data s, dan merubah data s ke dalam bentuk list
  for i in s.split():
    # check data sudah ada atau belum, jika ada +=1 jika belum =1 dan simpan nilai ke dictionary
    x[i] = 1 if (x.get(i) is None) else x.get(i)+1
  # kembalikan nilai dictionary
  return x

def urut_unik(s):
  # Tulis kode fungsi urut_unik() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # membuat set kosong agar data unik
  x = set()
  # melakukan looping string s list
  for i in s.split():
    # menambahkan data ke set
    x.add(i)
  # membuat list kosong
  ls = []
  # melakukan looping set
  for j in x:
    # menambahan data set ke data list
    ls.append(j)
  # mengurutkan list
  ls.sort()
  # mengembalikan nilai
  return ls

def read(filename):
  # Tulis kode fungsi read() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # membuat dictionary kosong
  x = {}
  # melakukan pembukaan file
  file = open(filename)
  # melakukan looping berdasarkan baris file
  for i in file:
    # memisahkan data dan membersihkan whitespace
    a = i.strip().split()
    # menambahkan data baru key and value
    x[a[0]]=a[1]
  # menutup file karena sudah selesai
  file.close()
  # mengembalikan hasil
  return x





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = hitung_kemunculan("pisang jambu apel jambu pisang jeruk")
  print(f"hitung_kemunculan('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: {{'pisang': 2, 'jambu': 2, 'apel': 1, 'jeruk': 1}})")
  print()
  r = urut_unik("pisang jambu apel jambu pisang jeruk")
  print(f"urut_unik('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: ['apel', 'jambu', 'jeruk', 'pisang'])")
  print()
  r = urut_unik('kecapi melon kecapi kecapi kecapi')
  print(f"urut_unik('kecapi melon kecapi kecapi kecapi') = {r} \n(solusi: ['kecapi', 'melon'])")
  print()
  r = read('data1.txt')
  print(f"read('data1.txt') = {r} \n(solusi: {{'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}}")
  print()
  r = read('data2.txt')
  print(f"read('nilai2.txt') = {r} \n(solusi: {{'711': 'Malaysia', '712': 'Singapura', '713': 'Indonesia', '814': 'USA', '815': 'Canada'}}")
  print()

if __name__ == '__main__':
  test()