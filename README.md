# Lampu-Lalu-Lintas-
Nama: Jihan Alya Naflah  
Nim: 2409116082

Kelas: C





![1](https://github.com/user-attachments/assets/5885784e-aecc-4599-9c6e-154eb888bf1b)


import time adalah perintah di Python untuk mengimpor modul bernama time. Modul time ini menyediakan berbagai fungsi yang berkaitan dengan pengelolaan waktu

![dua](https://github.com/user-attachments/assets/08020d68-e113-410c-a63c-b0f3cc33ca34)


status_lampu(detik, lampu) ini bertanggung jawab untuk menampilkan status lampu dan menghitung mundur durasi lampu tersebut.


detik: Menentukan berapa lama lampu akan aktif (dalam hitungan detik).

lampu: Menyimpan informasi tentang jenis lampu yang sedang aktif ("Lampu Merah", "Lampu Kuning", "Lampu Hijau").

Loop:
Selama nilai detik lebih besar dari 0, program akan mencetak status lampu bersama dengan countdown mundur.

Setelah setiap detik, fungsi time.sleep(1) digunakan untuk membuat program berhenti selama 1 detik, sehingga bisa mensimulasikan durasi lampu.

Countdown berkurang 1 detik setiap kali loop berjalan (melalui detik -= 1).

Ketika countdown mencapai 0, baris baru dicetak untuk memastikan tidak ada konflik dengan tampilan countdown berikutnya.


![3](https://github.com/user-attachments/assets/dd5872d8-fe4b-4635-9f25-9cf2a6e51f71)


traffic_light_simulation() ini akan menjalankan simulasi lampu lalu lintas. Fungsi ini menggunakan perulangan while True untuk memastikan program berjalan secara terus-menerus tanpa berhenti.

Lampu Merah: Menjalankan status_lampu(5, "Lampu Merah"), di mana Lampu Merah akan aktif selama 5 detik.
Lampu Kuning: Menjalankan status_lampu(2, "Lampu Kuning"), di mana Lampu Kuning akan aktif selama 2 detik.
Lampu Hijau: Menjalankan status_lampu(7, "Lampu Hijau"), di mana Lampu Hijau akan aktif selama 7 detik.
Simulasi akan terus mengulang siklus Lampu Merah, Lampu Kuning, dan Lampu Hijau.


![4](https://github.com/user-attachments/assets/2f43b5c7-b20f-443f-8d81-bccb63987744)


if __name__ == "__main__" Bagian ini memastikan bahwa jika file Python ini dijalankan secara langsung, maka fungsi traffic_light_simulation() akan dipanggil untuk memulai simulasi.


Program ini terus menerus melakukan pergantian antara tiga jenis lampu lalu lintas: Merah, Kuning, dan Hijau.

Setiap lampu memiliki durasi yang berbeda:
Lampu Merah: 5 detik
Lampu Kuning: 2 detik
Lampu Hijau: 7 detik

Selama setiap detik, status lampu saat ini bersama dengan jumlah detik tersisa akan ditampilkan pada layar. 
Countdown ini akan turun dari durasi awal (misalnya, 5 untuk Merah) hingga 0.
Setelah countdown selesai, program akan pindah ke lampu berikutnya.
