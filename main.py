# Aplikasi Kalkulator
while (True): 
    print(" ------------------------------- ");
    print("|     Aplikasi Kalkulator       |");
    print(" ------------------------------- ");
    print("Selamat Datang di Aplikasi Kalkulator sederhana\ndengan menggunakan bahasa python.");
    print("© Pasha Khatami Hasibuan");
    print("================================== \n");

    print(" ============================ ");
    print("|      Menu Kalkulator       |");
    print(" ============================ ");
    print("|  1. Penjumlahan  |   (+)   |");
    print("|  2. Pengurangan  |   (-)   |");
    print("|  3. Perkalian    |   (*)   |");
    print("|  4. Pembagian    |   (/)   |");
    print(" ---------------------------- ");
    print("|  5. Exit         |         |");
    print(" ============================ ");
    pilihanInput = input("Masukan pilihan yang ingin anda lakukan: ");
    pilihan = int(pilihanInput);
    
    try:
        if pilihan == 5:
          print("Terimakasih telah menggunakan aplikasi kalkulator python. Sampai Jumpa");
          break;
        elif pilihan < 1 or pilihan > 5:
          print("Pilihan tidak ada. Harap masukan dengan valid");
    except:
        print("Input tidak valid. Harap Masukan angka\n");
    
    if 1 <= pilihan <= 5 :
      bilangan1 = float(input("Masukan angka bilangan pertama: "));
      bilangan2 = float(input("Masukan angka bilangan kedua: "));
      if pilihan == 1:
        hasil = bilangan1 + bilangan2;
        print(f'Hasil dari Penjumlahan adalah {hasil}\n');
        continue;
      elif pilihan == 2:
        hasil = bilangan1 - bilangan2;
        print(f'Hasil dari Pengurangan adalah {hasil}\n');
        continue;
      elif pilihan == 3:
        hasil = bilangan1 * bilangan2;
        print(f'Hasil dari Perkalian adalah {hasil}\n');
        continue;
      elif pilihan == 4:
        if bilangan2 == 0:
          print('Bilangan tidak bisa dibagi dengan Nol. Hasil tidak Valid\n');
        else:
          hasil = bilangan1 / bilangan2;
          print(f'Hasil dari Pembagian adalah {hasil}\n');
          continue;
          
        if bilangan1 == " " or bilangan2 == " ":
            print("Input tidak boleh kosong. Harap coba lagi");
            continue;
      
      
    
    


