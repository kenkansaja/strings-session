import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """Ini akan membuatkan anda strings session

P -->> Untuk Pyrogram [https://docs.pyrogram.org]
T -->> Untuk Telethon [https://docs.telethon.dev]
"""

tutor = """
~ Pergi ke my.telegram.org
~ Login dengan akun telegram kamu
~ Klik di API Development Tools
~ Buat aplikasi baru, nanti masukan detail yang di perlukan
~ Sekarang cek pesan tersimpan kamu untuk melihat STRING_SESSION kamu
"""

template = """
Support: @kenkanasw
            
<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <b>Tolong hati-hati untuk melewati nilai ini untuk pihak ketiga</b>"""


print(docs)

while select != ("p", "t"):
    select = input("Silahkan pilih < p / t > : ").lower()
    if select == "t":
        print("""\nTelethon selected\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = int(input("Masukkan API_KEY disini: "))
        API_HASH = input("Masukkan API_HASH disini: ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = "Telethon session" + template.format(session_string)
            print("\nGenerating String Session...\n")
            client.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print("STRING_SESSION kamu, Berhasil dinkirim ke pesan tersimpan di Telegram kamu silahkan di cek.")
        break

    elif select == "p":
        print("""\nPyrogram selected.\nRunning script...""")
        time.sleep(1)
        print(tutor)
        with Client(
        "UserBot", 
        api_id=int(input("Masukkan API ID disini: ")),
        api_hash=input("Masukkan API HASH disini: ")) as pyrogram:
            saved_messages_template = "Pyrogram session" + template.format(pyrogram.export_session_string())
            print("\nGenerating String session...\n")           
            pyrogram.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1) 
            print("STRING_SESSION kamu berhasil di kirim ke pesan tersimpan di Telegram kamu silahkan cek.")
        break
    
    else:
        print("\nTolong pilih P atau T\n")
        time.sleep(1.5)
