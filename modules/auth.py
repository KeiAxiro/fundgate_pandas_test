from modules.data_store import baca_data

def proses_login(username_input, password_input):
    """
    Mengecek apakah username dan password ada di database users.
    """
    # 1. Ambil semua data user
    tabel_users = baca_data("users")
    
    # 2. Cari baris yang username DAN password-nya cocok
    # Ini cara filtering di Pandas yang mudah dibaca:
    hasil_pencarian = tabel_users[
        (tabel_users['username'] == username_input) & 
        (tabel_users['password'] == password_input)
    ]
    
    # 3. Cek apakah hasil pencarian kosong?
    if hasil_pencarian.empty:
        return None  # Gagal login
    else:
        # Ambil data orang pertama yang ditemukan
        # iloc[0] artinya ambil baris index ke-0 (baris pertama)
        data_user = hasil_pencarian.iloc[0]
        
        # Ubah jadi dictionary python biasa biar gampang dipakai
        # Contoh: {'username': 'kei', 'role': 'kepala_divisi', ...}
        return data_user.to_dict()