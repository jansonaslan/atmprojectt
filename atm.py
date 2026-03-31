from datetime import datetime

class Transaksi:
    def __init__(self, jenis, jumlah, saldo):
        self.tanggal = datetime.now()
        self.jenis = jenis
        self.jumlah = jumlah
        self.saldo = saldo

    def tampilkan(self):
        print(f"{self.tanggal} | {self.jenis} | {self.jumlah} | Saldo: {self.saldo}")


class Rekening:
    def __init__(self, no_rekening, saldo=0):
        self.no_rekening = no_rekening
        self.saldo = saldo
        self.riwayat = []

    def setor(self, jumlah):
        self.saldo += jumlah
        self.riwayat.append(Transaksi("Setor", jumlah, self.saldo))
        print("Setor berhasil")

    def tarik(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            self.riwayat.append(Transaksi("Tarik", jumlah, self.saldo))
            print("Tarik berhasil")
        else:
            print("Saldo tidak cukup")

    def transfer(self, rekening_tujuan, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            rekening_tujuan.saldo += jumlah
            self.riwayat.append(Transaksi("Transfer Keluar", jumlah, self.saldo))
            rekening_tujuan.riwayat.append(Transaksi("Transfer Masuk", jumlah, rekening_tujuan.saldo))
            print("Transfer berhasil")
        else:
            print("Saldo tidak cukup")

    def cek_saldo(self):
        print("Saldo:", self.saldo)

    def riwayat_transaksi(self):
        print("=== Riwayat Transaksi ===")
        for t in self.riwayat:
            t.tampilkan()

class Nasabah:
    def __init__(self, nama, pin, rekening):
        self.nama = nama
        self.pin = pin
        self.rekening = rekening

    def verifikasi_pin(self, pin):
        return self.pin == pin


class Bank:
    def __init__(self):
        self.daftar_nasabah = []

    def register(self, nama, pin):
        no_rekening = str(len(self.daftar_nasabah) + 1).zfill(5)
        rekening = Rekening(no_rekening, 0)
        nasabah = Nasabah(nama, pin, rekening)
        self.daftar_nasabah.append(nasabah)
        print("Register berhasil. No Rekening:", no_rekening)

    def login(self, nama, pin):
        for nasabah in self.daftar_nasabah:
            if nasabah.nama == nama and nasabah.pin == pin:
                print("Login berhasil")
                return nasabah
        print("Login gagal")
        return None

class ATM:
    def __init__(self, nasabah, bank):
        self.nasabah = nasabah
        self.bank = bank

    def menu(self):
        while True:
            print("\n=== MENU ATM ===")
            print("1. Cek Saldo")
            print("2. Setor Tunai")
            print("3. Tarik Tunai")
            print("4. Transfer")
            print("5. Riwayat Transaksi")
            print("6. Keluar")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                self.nasabah.rekening.cek_saldo()

            elif pilihan == "2":
                jumlah = int(input("Jumlah setor: "))
                self.nasabah.rekening.setor(jumlah)

            elif pilihan == "3":
                jumlah = int(input("Jumlah tarik: "))
                self.nasabah.rekening.tarik(jumlah)

            elif pilihan == "4":
                tujuan = input("No rekening tujuan: ")
                jumlah = int(input("Jumlah transfer: "))
                rekening_tujuan = None

                for n in self.bank.daftar_nasabah:
                    if n.rekening.no_rekening == tujuan:
                        rekening_tujuan = n.rekening

                if rekening_tujuan:
                    self.nasabah.rekening.transfer(rekening_tujuan, jumlah)
                else:
                    print("Rekening tidak ditemukan")

            elif pilihan == "5":
                self.nasabah.rekening.riwayat_transaksi()

            elif pilihan == "6":
                print("Keluar dari ATM")
                break

            else:
                print("Menu tidak ada")


bank = Bank()

while True:
    print("\n=== SISTEM ATM ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama: ")
        pin = input("PIN: ")
        bank.register(nama, pin)

    elif pilih == "2":
        nama = input("Nama: ")
        pin = input("PIN: ")
        user = bank.login(nama, pin)

        if user:
            atm = ATM(user, bank)
            atm.menu()

    elif pilih == "3":
        break

    else:
        print("Pilihan tidak ada")