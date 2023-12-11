import random
from scapy.all import IP, TCP, sr1, send, wrpcap

HTTP_PORT = 80

def send_http_get(dst, src):
    get_str = f'GET / HTTP/1.1\r\nHost: {dst}\r\nAccept-Encoding: gzip, deflate\r\n\r\n'
    #sending syn packet to establish tcp
    syn = IP(dst=dst, src=src) / TCP(sport=random.randint(1025, 65500), dport=80, flags='S')
    #receive the syn ack from server
    syn_ack = sr1(syn)

    if syn_ack:
        # Send ACK
        ack = IP(dst=dst, src=src) / TCP(dport=80, sport=syn_ack[TCP].dport,
                                                seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A')
        send(ack)

        #sending http get
        http_get = IP(dst=dst, src=src) / TCP(dport=80, sport=syn_ack[TCP].dport,
                                                     seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='PA') / get_str
        send(http_get)
        
        return http_get

def send_http_traffic(src: str, dst: str, pkt_cnt: int, filename: str) -> None:
    """
    src: source IP string "xxx.xxx.xxx.xxx"
    dst: destination IP string "xxx.xxx.xxx.xxx"
    pkt_cnt: amount of packets to send
    filename: the name of the packet capture file to save packets to
    """
    pkts = [] 
    #IP(src=src, dst=dst)/TCP(sport=1234, dport=HTTP_PORT) 
    for _ in range (pkt_cnt):
        pkt = send_http_get(src=src, dst=dst)
        pkts.append(pkt)
        send(pkt)
    wrpcap(filename, pkts)
