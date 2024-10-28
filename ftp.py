from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket

# FTP server ayarları
FTP_USER = "user"       
FTP_PASSWORD = "password"   
FTP_DIRECTORY = "."         
FTP_PORT = 2121            

def start_ftp_server():
    # FTP için kullanıcı yetkilendirmesini ayarla
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm="elradfmw") # Tüm izinler verildi (okuma, yazma vs.)

    handler = FTPHandler
    handler.authorizer = authorizer

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    server = FTPServer((local_ip, FTP_PORT), handler)
    print(f"FTP sunucusu başlatıldı! Bağlantı için ftp://{local_ip}:{FTP_PORT}")
    print(f"Kullanıcı adı: {FTP_USER}")
    print(f"Şifre: {FTP_PASSWORD}")
    server.serve_forever()

# FTP sunucusunu başlat
start_ftp_server()
