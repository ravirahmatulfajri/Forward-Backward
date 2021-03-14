# TUGAS 1
NAMA : RAVI RAHMATUL FAJRI
NPM : 1184040
KELAS : D4 TEKNIK INFORMATIKA 3A
MATA KULIAH : SISTEM PAKAR
DOSEN PENGAMPU : M NURKAMAL F, S.T., M.T.

# forked from asksom/Forward-Backward
https://github.com/asksom/Forward-Backward

# Forward-Backward
Implementasu sederhana forward-backward algorithm untuk TDT4171: Methods dalam AI

Algoritma forward-backward terdiri dari dua bagian, 
1. algoritma forward yang digunakan untuk pemfilteran, sebuah proses untuk menghitung secara rekursif probabilitas gabungan P (x <sub> t </sub>, y <sub> 1: t </sub>) dan
2. algoritma backward yang digunakan untuk menghaluskan, sebuah proses yang bergerak mundur untuk mengedit probabilitas menjadi nilai yang lebih akurat.

Settingnya adalah sebagai berikut; seorang pria duduk di bunker, tidak mampu mengamati dunia luar. Dia penasaran apakah di luar sedang hujan atau tidak.
Informasi satu-satunya tentang dunia adalah melihat bosnya, yang cukup beruntung tidak tinggal di bunker, membawa atau tidak membawa payung.

Jika hujan ada kemungkinan 90% bosnya membawa payung, jika tidak hujan ada peluang 20% ​​dia membawa payung. Ada juga kemungkinan 70% cuaca akan identik dengan hari sebelumnya.

Diberikan peluang 50-50 hari pertama.


Bagian a):
Variabel yang tidak dapat diamati adalah cuaca, atau lebih tepatnya, apakah sedang hujan atau tidak.

Variabel yang dapat diamati adalah apakah bos protagonis memiliki payung atau tidak.

Model dinamis / transisi disajikan sebagai matriks dalam kode.


Asumsi dalam model ini adalah bahwa hujan dan bukan hujan memiliki kemungkinan yang sama pada keadaan awal, yang belum tentu benar. Lebih jauh orang dapat berargumen bahwa ini adalah pandangan yang sangat disederhanakan tentang bagaimana cuaca beroperasi di dunia nyata. Model ini mengasumsikan matriks transisi konstan serta bos yang sangat dapat diprediksi.
