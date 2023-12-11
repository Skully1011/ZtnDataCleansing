# That is a beta version so proceed carefully, please.

from scapy.all import IP, ICMP, TCP, wrpcap, RandIP, send
import sys

HTTP_PORT = 80

def main():
    if len(sys.argv) < 4:
        print('Usage: python3 pcap_generator.py <destination IP> <number of packets> <filename> ')
        exit(1)

    dst_ip = str(sys.argv[1])
    pkt_cnt= int(sys.argv[2])
    filename = str(sys.argv[3])

    time = 0.00114108 *pkt_cnt + 0.157758
    minutes = time/60
    print('Generating packets, it will take %s seconds, moreless (%s, minutes)' % (time, minutes))

    pkts = [IP(dst=dst_ip)/ICMP() for i in range (pkt_cnt)]
    for pkt in pkts:
        #s_addr = RandIP()   #random Ip address
        #pkt =IP(src=s_addr, dst=dst_ip)/ TCP(sport =sport, dport=dport, seq= 1505066, flags="S")
        send(pkt)
    wrpcap(filename, pkts)

    print('%s packets generated.' % (pkt_cnt))   

def send_traffic(src: str, dst: str, pkt_cnt: int, filename: str) -> None:
    """
    src: source IP string "xxx.xxx.xxx.xxx"
    dst: destination IP string "xxx.xxx.xxx.xxx"
    pkt_cnt: amount of packets to send
    filename: the name of the packet capture file to save packets to
    """
    pkts = [IP(src=src, dst=dst)/TCP(sport=1234, dport=HTTP_PORT) for _ in range (pkt_cnt)]
    for pkt in pkts:
        send(pkt)
    wrpcap(filename, pkts)

if __name__ == "__main__":
    main()