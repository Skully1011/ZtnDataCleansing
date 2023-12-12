import time, random
from send_http import send_http_traffic
from SYN_flood import syn_flood_attack

LOWER_LIM = 3
UPPER_LIM = 10.01
WEB_NODE_IP="192.168.1.2"
DEVIL_NODE_IP="192.168.1.5"

PCAP_FILE_NAME = "NetTraffic.pcap"

def main():
    """
    Sends a random amount [25-100] of generated GET requests to a web server host
    and waits a random float amount of time before sending the next transmission

    alternatively also has a chance to execute a SYN flood attack where it will
    send a random number [1000,10000] of pkts to execute a SYN flood

    NOTE This executes indefinitely
    """
    while True:
        if random.choice([0,1]):
            # send a random amount of packets
            # pkt = session_cnt * 4; each session requires a syn, synack, ack, then http get
            session_cnt = random.randint(25,100)
            send_http_traffic(DEVIL_NODE_IP, WEB_NODE_IP, session_cnt, PCAP_FILE_NAME)
        else:
            syn_flood_attack(WEB_NODE_IP, random.randint(100,1000))

        # pick random amount of time to wait between next batch of traffic
        rand_float = random.uniform(LOWER_LIM, UPPER_LIM)
        time.sleep(rand_float)
    

if __name__ == "__main__":
    main()