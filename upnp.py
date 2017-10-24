import socket

class UPNP:
    @staticmethod
    def discover():
        msg = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'HOST:239.255.255.250:1900\r\n' \
        'ST:upnp:rootdevice\r\n' \
        'MX:2\r\n' \
        'MAN:"ssdp:discover"\r\n' \
        '\r\n'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.settimeout(10)
        s.sendto(msg.encode('utf-8'), ('239.255.255.250', 1900) )
        response=[]
        try:
            while True:
                data, addr = s.recvfrom(65507)
                print(data,addr)
                response.append([addr, data])
        except socket.timeout:
            pass
        return response
