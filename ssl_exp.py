import datetime
import socket
import ssl
def expiry_date(hostname: str, port: str = '443'):    
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssl_info = ssock.getpeercert()
            expiry_date = datetime.datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
            print(f'{hostname} expires on {expiry_date}')
            return expiry_date
if __name__ == '__main__':
    a=str(input('Enter the hostname/website: '))
    expiry_date(a)