# FileSharing

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.. 😇.

##

**Jika Anda memerlukan tambahan module lagi dalam repo atau Jika Anda menemukan bug, silahkan report di group [@PocongUserbot](https://www.telegram.dog/PocongUserbot)**

### Features
- Sepenuhnya dapat dicustom.
- Dapat di-deploy di heroku & vps.
- Pesan sambutan & Forcesub yang dapat dicustom.
- Lebih dari satu Posting dalam Satu Link (batch).
- Fleksibel FSUB Button bisa 1 button atau 2 button menyesuaikan dengan var yang di isi.

### Setup

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel ForceSub tambahkan bot sebagai ADMIN
- Tambahkan bot ke Group ForceSub tambahkan bot sebagai ADMIN


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<details>
    <summary> <b>🔗 Deploy On Heroku</b></summary><br/>


<p align="center"><a href="https://userbotindo.tech"><img src="https://img.shields.io/badge/Deploy%20Lewat%20Web%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200"" /></a></p>

<p align="center"><a href="https://telegram.dog/XTZ_HerokuBot?start=SnN0a3l5L0ZpbGVTaGFyaW5nIG1hc3Rlcg"><img src="https://img.shields.io/badge/Deploy%20Lewat%20Bot%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200"" /></a></p>

</details>

<details>
    <summary> <b>🔗 Deploy In Your VPS<b></summary><br/>
    
    
```
bash
git clone https://github.com/Jstkyy/FileSharing
cd FileSharing
pip3 install -r requirements.txt
cp sample_config.env config.env
# edit config.env Anda dan isi VARS menggunakan nano config.env CTRL + S untuk menyimpan VARS Anda, 
# gunakan CTRL + X untuk keluar dan kembali ke direktori FileSharing
bash start
```

</details>

        
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


### Admin Commands

```
/start - mulai bot atau dapatkan postingan

/batch - buat link untuk lebih dari satu posting

/genlink - buat link untuk satu posting

/users - lihat statistik pengguna bot

/broadcast - menyiarkan/broadcast pesan apa pun ke pengguna bot

/ping - untuk mengecek bot
```

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `OWNER_ID` Masukan User ID Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin BOT [Hanya dapat membuat link]
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/Jstkyy/FileSharing/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB_CHANNEL` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB_GROUP` Masukan ID dari Group Untuk Wajib Subscribenya

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/Jstkyy/FileSharing/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Bergabunglah di [Group Telegram ](https://www.telegram.dog/PocongUserbot) Untuk Dukungan/Bantuan Dan Join [Channel](https://www.telegram.dog/Pocongproject) untu info Update bot.   
   
Laporkan Bug, Berikan Permintaan Fitur Di sana.. 

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- CodeXBotz • [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot)
- mrismanaziz • [FILE-SHARING-MAN](https://github.com/mrismanaziz/File-Sharing-Man/)
- Our Support Group Members


   **Berikan Bintang Repo ini jika Anda menyukainya ⭐⭐⭐⭐⭐**

