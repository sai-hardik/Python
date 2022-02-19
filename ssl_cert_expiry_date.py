import ssl
import socket
import datetime

url = input("Enter the url of the website :")

def ssl_expiry_date(host, port=443):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=host,
    )
  
    
    conn.connect((host, port))
    ssl_info = conn.getpeercert()
    x = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
    return x

print(ssl_expiry_date(url))



