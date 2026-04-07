import sys
accounts = {
    "janson" : {"pin": "123456", "balance": 100000000},
    "griselda" : {"pin": "654321", "balance" : 90000000},
    "arthur" : {"pin": "111111", "balance" : 85000000},
}
#ini adalah asal dari lang_map
LANG = {
    "id": {
        "masukkan_nama_akun_anda : " : "masukkan nama akun anda : ",
        "masukkan_pilihan : " : "masukkan pilihan : ",
        "nama_akun": "nama akun",
        "terima_kasih" : "terima kasih",
        "lanjutkan (y/n) : ": "lanjutkan (y/n) : ",
        "pembayaran_sukses_terima_kasih" : "pembayaran sukses, terima kasih",
        "saldo_anda : Rp. ": "saldo anda : Rp. {}",
        "cek_saldo": "cek saldo",
        "setor": "setor",
        "tarik": "tarik",
        "keluar": "keluar",
        "input_pilihan : ": "pilih menu : ",
        "login_berhasil": "login berhasil",
        "=== PILIH_MENU ===": "=== PILIH MENU ===",
        "=== PILIH_BANK ===": "=== PILIH BANK ===",
        "menu": "menu",
        "tarik_tunai": "tarik tunai",
        "cek_saldo": "cek saldo",
        "informasi_akun": "informasi akun",
        "bayar": "bayar",
        "masukkan_username : ": "masukkan username : ",
        "masukkan_PIN : ": "masukkan PIN : ",
        "username_tidak_ditemukan": "username tidak ditemukan",
        "pilih_bahasa (1/2/3) : ": "pilih bahasa (1/2/3) : ",
        "bahasa_tidak_valid": "pilihan bahasa tidak valid, menggunakan indonesia ",
        "pilih_bank": "pilih bank",
        "maaf_pilihan_anda_tidak_ada_di_sistem": "maaf pilihan anda tidak ada di sistem",
        "selamat_datang_di_BRI": "selamat datang di BRI",
        "selamat_datang_di_BCA": "selamat datang di BCA",
        "selamat_datang_di_BNI": "selamat datang di BNI",
        "selamat_datang_di_BSI": "selamat datang di BSI",
        "selamat_datang_di_BTN": "selamat datang di BTN",
        "masukkan_nominal_yang_akan_anda_transfer : ": "masukkan nominal yang akan anda transfer : ",
        "nominal_yang_akan_anda_transfer_adalah ": "nominal yang akan anda transfer adalah ",
        "lanjutkan": "lanjutkan",
        "transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda": "transaksi dibatalkan, silahkan ambil kartu atm anda",
        "silahkan_ambil_kartu_atm_anda": "silahkan ambil kartu atm anda",
        "akun_anda_dalam_proteksi_bank": "akun anda dalam proteksi bank",
        "maaf_nama_anda_tidak_tersedia": "maaf nama anda tidak tersedia",
        "akunmu_diblokir_silahkan_hubungi_pihak_bank": "akunmu diblokir silahkan hubungi pihak bank",
        "maaf_pin_anda_salah_silahkan_coba_lagi": "maaf pin anda salah silahkan coba lagi {}",
        "masukkan_nominal_setor": "masukkan nominal setor",
        "setor_berhasil": "setor berhasil",
        "masukkan_nominal_tarik : ": "masukkan nominal tarik : ",
        "saldo_tidak_cukup": "saldo tidak cukup",
        "penarikan_berhasil": "penarikan berhasil",
        "pin_anda_benar_selamat_datang": "pin anda benar, selamat datang",
        "masukkan_nama_rekening_tujuan": "masukkan nama rekening tujuan",
        "rekening_tujuan_tidak_ditemukan": "rekening tujuan tidak ditemukan",
        "tidak_bisa_transfer_ke_rekening_sendiri": "tidak bisa transfer ke rekening",
        "masukkan_nominal_yang_akan_anda_transfer": "masukkan nominal yang akan anda transfer",
        "transfer_berhasil_saldo_anda_sekarang : Rp. " : "transfer berhasil, saldo anda sekarang : Rp. {}",
        "transfer_antar_rekening" : "transfer antar rekening", 
    },

    "en": {
        "masukkan_nama_akun_anda : " : "input your account name : ",
        "masukkan_pilihan : " : "input choice : ",
        "nama_akun": "account name",
        "terima_kasih" : "thank you",
        "lanjutkan (y/n) : ": "continue (y/n) : ",
        "pembayaran_sukses_terima_kasih" : "payment success, thank you",
        "saldo_anda : Rp. ": "your balance : Rp. {}",
        "cek_saldo": "balance check",
        "setor": "deposit",
        "tarik": "withdraw",
        "keluar": "exit",
        "input_pilihan : ": "choose menu : ",
        "login_berhasil": "login success",
        "=== PILIH_MENU ===": "=== CHOOSE MENU ===",
        "=== PILIH_BANK ===": "=== CHOOSE BANK ===",
        "menu": "menu",
        "tarik_tunai": "cash withdrawal",
        "cek_saldo": "balance check",
        "informasi_akun": "account information",
        "bayar": "pay",
        "masukkan_username : ": "input username : ",
        "masukkan_PIN : ": "input pin : ",
        "username_tidak_ditemukan": "username is not found",
        "pilih_bahasa (1/2/3) : ": "choose language (1/2/3) : ",
        "bahasa_tidak_valid": "language invalid, use indonesian ",
        "pilih_bank": "choose bank",
        "maaf_pilihan_anda_tidak_ada_di_sistem": "sorry your choice not in the system",
        "selamat_datang_di_BRI": "welcome to BRI",
        "selamat_datang_di_BCA": "welcome to BCA",
        "selamat_datang_di_BNI": "welcome to BNI",
        "selamat_datang_di_BSI": "welcome to BSI",
        "selamat_datang_di_BTN": "welcome to BTN",
        "masukkan_nominal_yang_akan_anda_transfer": "enter the amount you want to transfer",
        "nominal_yang_akan_anda_transfer_adalah ": "nominal yang akan anda transfer adalah",
        "lanjutkan": "continue",
        "transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda": "transaction is cancelled, please take your atm card",
        "akun_anda_dalam_proteksi_bank": "you account is under bank protection",
        "maaf_nama_anda_tidak_tersedia": "sorry your name is not available",
        "akunmu_diblokir_silahkan_hubungi_pihak_bank": "your accoount is blocked please call bank",
        "maaf_pin_anda_salah_silahkan_coba_lagi": "sorry your pin is wrong please try again {}" ,
        "masukkan_nominal_setor": "input deposit nominal",
        "setor_berhasil": "deposit is successfull",
        "masukkan_nominal_tarik : ": "input withdrawal nominal : ",
        "saldo_tidak_cukup": "balance is not enough",
        "penarikan_berhasil": "withdrawall successfull",
        "pin_anda_benar_selamat_datang": "your pin is true, welcome",
        "masukkan_nama_rekening_tujuan": "input ",
        "rekening_tujuan_tidak ditemukan" : "destination account is not found",

    },

    "jv": {
        "masukkan_nama_akun_anda : " : "lebokke jeneng akunmu : ",
        "masukkan_pilihan : " : "lebokke pilihan : ",
        "nama_akun": "jeneng akun",
        "terima_kasih" : "matur nuwun",
        "lanjutkan (y/n) : ": "lanjutke (y/n) : ",
        "pembayaran_sukses_terima_kasih" : "pembayaran sukses, matur nuwun",
        "saldo_anda : Rp. ": "saldomu : Rp. {}",
        "cek_saldo": "ngecek saldo",
        "setor": "nyetor",
        "tarik": "narik",
        "keluar": "metu",
        "input_pilihan : ": "pilih menu : ",
        "login_berhasil": "login sukses",
        "=== PILIH_MENU ===": "=== MILIH MENU ===",
        "=== PILIH_BANK ===": "=== MILIH BANK ===",
        "menu": "menu",
        "tarik_tunai": "narik tunai",
        "cek_saldo": "ngecek saldo",
        "informasi_akun": "informasi akun",
        "bayar": "mbayar",
        "masukkan_username : ": "lebokke jeneng : ",
        "masukkan_PIN : ": "lebokke pin : ",
        "username_tidak_ditemukan": "jenengmu ra ketemu cok",
        "pilih_bahasa (1/2/3) : ": "milih bahasa (1/2/3) : ",
        "bahasa_tidak_valid": "bahasa ora cocok, nganggo indonesia ",
        "pilih_bank": "milih bank",
        "maaf_pilihan_anda_tidak_ada_di_sistem": "ngapurane pilihanmu ora ono neng sistem",
        "selamat_datang_di_BRI": "sugeng rawuh ing BRI",
        "selamat_datang_di_BCA": "sugeng rawuh ing BCA",
        "selamat_datang_di_BNI": "sugeng rawuh ing BNI",
        "selamat_datang_di_BSI": "sugeng rawuh ing BSI",
        "selamat_datang_di_BTN": "sugeng rawuh ing BTN",
        "masukkan_nominal_yang_akan_anda_transfer : ": "lebokke nominal seng arep kok transfer : ",
        "nominal_yang_akan_anda_transfer_adalah ": "nominal seng arep kok transfer yaiku",
        "lanjutkan": "lanjutke",
        "transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda": "transaksi dibatalke, mangga jupuk kartu atm e sampean",
        "akun_anda_dalam_proteksi_bank": "akunmu dilindungi bank",
        "maaf_nama_anda_tidak_tersedia": "ngapurane jenengmu ora ono",
        "masukkan_nama_akun_anda": "lebokke jeneng akunmu",
        "akunmu_diblokir_silahkan_hubungi_pihak_bank": "akunmu diblokir hubungi bank yo ",
        "maaf_pin_anda_salah_silahkan_coba_lagi": "ngapurane pin mu salah dijajal maneh yo {}" ,
        "masukkan_nominal_setor": "lebokke nominal seng arep kok setor",
        "setor_berhasil": "setoran sukses",
        "masukkan_nominal_tarik : ": "lebokke nominal seng arep ditarik : ",
        "saldo_tidak_cukup": "saldomu ra cukup cok",
        "penarikan_berhasil": "penarikan sukses",
        "pin_anda_benar_selamat_datang": "pin mu bener, sugeng rawuh",
    },
}

print("selamat datang di mandiri")
print("transaksi bebas biaya admin")

print("Bahasa : ")
print("1. Indonesia")
print("2. Inggris")
print("3. Jawa")
lang_input = input("pilih bahasa (1/2/3) : ")
lang_map = {"1": "id", "2": "en", "3": "jv"}
lang_code = lang_map.get(lang_input, "id") #disini dia mengambil kode dari lang map, apabila kode tidak ditemukan, maka pakai "id"
if lang_code not in LANG:
    print("pilihan bahasa tidak valid anda akan menggunakan bahasa indonesia")
    lang_code = "1"
    
T = LANG[lang_code]
#T untuk semua teks yang dipakai

def authenticate(acct_id, max_attempts=3):
    attempts = max_attempts
    while attempts > 0:
        pin = input(T["masukkan_PIN : "])
        if pin == accounts[acct_id]["pin"]:
            print(T["pin_anda_benar_selamat_datang"])
            return True
        attempts -= 1
        print(T["maaf_pin_anda_salah_silahkan_coba_lagi"])
    print(T["akunmu_diblokir_silahkan_hubungi_pihak_bank"])
    return False

def validate_nominal(nominal):
    try:
        n = int(nominal)
        if n <= 0:
            return False , "nominal harus > 0"
        return True, ""
    except:
        return False, "nominal harus angka"
    
def informasi_akun():
    print(T["nama_akun"])

    pilih = input(T["masukkan_nama_akun_anda : "])

    if pilih == "janson":
        print(T["akun_anda_dalam_proteksi_bank"])
    elif pilih == "griselda":
        print(T["akun_anda_dalam_proteksi_bank"])
    elif pilih == "arthur":
        print(T["akun_anda_dalam_proteksi_bank"])
    else:
        print(T["maaf_nama_anda_tidak_tersedia"])

def cek_saldo(user):
    print(T["saldo_anda : Rp. "].format(accounts[user]['balance']))

def setor(user):
    nominal = input(T["masukkan_nominal_setor : "])
    ok, msg = validate_nominal(nominal)
    if not ok:
        print(msg)
        return
    
    n = int(nominal)
    accounts[user]["balance"] += n #setor dia +
    print(T["setor_berhasil"])
    cek_saldo(user)

def tarik(user):
    nominal = input(T["masukkan_nominal_tarik : "])
    ok, msg = validate_nominal(nominal)
    #ok (jika dia true/false), msg (pesan error kalau tidak valid)
    if not ok:
        print(msg)
        return
    
    n = int(nominal)

    if n > accounts[user]["balance"]:
        print(T["saldo_tidak_cukup"])
        return
    
    accounts[user]["balance"] -= n #tarik dia -
    print(T["penarikan_berhasil"])
    cek_saldo(user)

def keluar():
    print(T["terima_kasih"])

def bayar():
        print("\n" + T["=== PILIH_BANK ==="])
        print("1. BRI")
        print("2. BCA")
        print("3. BNI")
        print("4. BSI")
        print("5. BTN")
        pilih = input(T["masukkan_pilihan : "])

        if pilih == "1":
            print(T["selamat_datang_di_BRI"])
            nominal_transfer = input(T["masukkan_nominal_yang_akan_anda_transfer : "])
            print(T["nominal_yang_akan_anda_transfer_adalah "] + nominal_transfer)
            pilih = str(input(T["lanjutkan (y/n) : "]))
            if pilih == "y":
                print(T["pembayaran_sukses_terima_kasih"])
            elif pilih == "n":
                print(T["transaksi_dibatalkan"])
                print(T["transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda"])
                

        elif pilih == "2":
            print(T["selamat_datang_di_BCA"])
            nominal_transfer = input(T["masukkan_nominal_yang_akan_anda_transfer : "])
            print(T["nominal_yang_akan_anda_transfer_adalah "] + nominal_transfer)
            pilih = str(input(T["lanjutkan (y/n) : "]))
            if pilih == "y":
                print(T["pembayaran_sukses_terima_kasih"])
            elif pilih == "n":
                print(T["transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda"])
        
        elif pilih == "3":
            print(T["selamat_datang_di_BNI"])
            nominal_transfer = input(T["masukkan_nominal_yang_akan_anda_transfer : "])
            print(T["nominal_yang_akan_anda_transfer_adalah "] + nominal_transfer)
            pilih = str(input(T["lanjutkan (y/n) : "]))
            if pilih == "y":
                print(T["pembayaran_sukses_terima_kasih"])
            elif pilih == "n":
                print(T["transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda"])
        
        elif pilih == "4":
            print(T["selamat_datang_di_BSI"])
            nominal_transfer = input(T["masukkan_nominal_yang_akan_anda_transfer : "])
            print(T["nominal_yang_akan_anda_transfer_adalah "] + nominal_transfer)
            pilih = str(input(T["lanjutkan (y/n) : "]))
            if pilih == "y":
                print(T["pembayaran_sukses_terima_kasih"])
            elif pilih == "n":
                print(T["transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda"])

        elif pilih == "5":
            print(T["selamat_datang_di_BTN"])
            nominal_transfer = input(T["masukkan_nominal_yang_akan_anda_transfer : "])
            print(T["nominal_yang_akan_anda_transfer_adalah "] + nominal_transfer)
            pilih = str(input(T["lanjutkan (y/n) : "]))
            if pilih == "y":
                print(T["pembayaran_sukses_terima_kasih"])
            elif pilih == "n":
                print(T["transaksi_dibatalkan_silahkan_ambil_kartu_atm_anda"])
        
        else:
            print(T["maaf_pilihan_anda_tidak_ada_di_sistem"])

def transfer_antar_rekening(user):
    rekening_tujuan = input(T["masukkan_nama_rekening_tujuan"]).strip()
    if rekening_tujuan not in accounts:
        print(T["rekening_tujuan_tidak_ditemukan"])
    if rekening_tujuan == user:
        print(T["tidak_bisa_transfer_ke_rekening_sendiri"])
        return
    
    nominal = input(T["masukkan_nominal_yang_akan_anda_transfer : "])
    ok, msg = validate_nominal(nominal)
    if not ok:
        print(msg)
        return

    n = int(nominal)
    if n > accounts[user]["balance"]:
        print(T["saldo_tidak_cukup"])
        return
    
    accounts[user]["balance"] -= n
    accounts[rekening_tujuan]["balance"] += n

    print(T["transfer_berhasil_saldo_anda_sekarang: Rp. "] + {accounts[user['balance']]})

def menu(user):
    while True:
        print("\n" + T["=== PILIH_MENU ==="])
        print("1.", T["tarik_tunai"])
        print("2.", T["cek_saldo"])
        print("3.",  T["informasi_akun"])
        print("4.", T["bayar"])
        print("5.", T["transfer_antar_rekening"])
        print("6.", T["keluar"])
        pilih = input(T["input_pilihan : "]).strip()

        if pilih == "1":
            tarik(user)
        elif pilih == "2":
            cek_saldo(user)
        elif pilih == "3":
            informasi_akun()
        elif pilih == "4":
            bayar()
        elif pilih == "5":
            transfer_antar_rekening(user)
        elif pilih == "6":
            keluar()
        else:
            print(T["pilihan_tidak_valid"])

while True:
    username = input(T["masukkan_username : "]).strip()
    if username not in accounts:
        print(T["username_tidak_ditemukan"])
        continue

    if authenticate(username):
        menu(username)
        break
    else:
        print(T["akunmu_diblokir_silahkan_hubungi_pihak_bank"])
        break



    

