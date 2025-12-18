from modules.data_store import baca_data, simpan_data

def menu_manajer(user_sedang_login):
    while True:
        print("\n=== MENU MANAJER KEUANGAN ===")
        print("1. Cek Pengajuan Masuk (Persetujuan)")
        print("0. Kembali")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            proses_persetujuan_dana()
        elif pilihan == "0":
            break

def proses_persetujuan_dana():
    tabel_pengajuan = baca_data("pengajuan")
    
    # 1. Filter: Cari yang statusnya masih 'Menunggu'
    data_pending = tabel_pengajuan[tabel_pengajuan['status'] == 'Menunggu']
    
    if data_pending.empty:
        print("Tidak ada pengajuan yang perlu diproses saat ini.")
        return

    # Tampilkan data yang menunggu
    print("\n--- DAFTAR PENGAJUAN MENUNGGU ---")
    print(data_pending[['id', 'divisi', 'nominal', 'kategori']].to_string(index=False))
    
    # Minta input ID mana yang mau diurus
    id_target = input("\nMasukkan ID Pengajuan yang mau diproses: ")
    
    # Cek apakah ID ada di tabel?
    # .values itu mengubah kolom jadi list biasa
    if id_target in tabel_pengajuan['id'].values:
        
        keputusan = input("Ketik '1' untuk SETUJU atau '2' untuk TOLAK: ")
        status_baru = ""
        
        if keputusan == "1":
            status_baru = "Disetujui"
        elif keputusan == "2":
            status_baru = "Ditolak"
        else:
            print("Input salah. Batal.")
            return

        # LOGIKA UPDATE DATA (Penting!)
        # Cari baris dimana kolom 'id' sama dengan 'id_target', 
        # lalu ubah kolom 'status' menjadi status_baru
        tabel_pengajuan.loc[tabel_pengajuan['id'] == id_target, 'status'] = status_baru
        
        simpan_data("pengajuan", tabel_pengajuan)
        print(f"Berhasil! Pengajuan {id_target} statusnya sekarang: {status_baru}")
        
    else:
        print("ID tidak ditemukan. Pastikan ketik ID dengan benar (misal: REQ-123456)")