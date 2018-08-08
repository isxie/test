#coding=utf-8
#!/usr/bin/python
import socket
from pinject import IP, UDP

payload = 'enhe'
src = {'ip':'8.8.9.9','port':555}
dst = {'ip':'122.226.223.164','port':666}

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
udp = UDP(src['port'], dst['port'], payload).pack(src['ip'], dst['ip'])
ip = IP(src['ip'], dst['ip'], udp, proto=socket.IPPROTO_UDP).pack()
sock.sendto(ip+udp+payload,(dst['ip'], dst['port']))
