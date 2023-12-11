import time, random
from send_http import send_http_traffic

LOWER_LIM = 0
UPPER_LIM = 5.01
WEB_NODE_IP="192.168.1.2"
ANGEL_NODE_IP="192.168.1.4"

PCAP_FILE_NAME = "NetTraffic.pcap"

def main():
    """
    Sends a random amount [25-100] of generated GET requests to a web server host
    and waits a random float amount of time before sending the next transmission

    NOTE This executes indefinitely
    """
    while True:
        # send a random amount of packets
        # pkt = session_cnt * 4; each session requires a syn, synack, ack, then http get
        session_cnt = random.randint(25,100)
        send_http_traffic(ANGEL_NODE_IP, WEB_NODE_IP, session_cnt, PCAP_FILE_NAME)
        # pick random amount of time to wait between next batch of traffic
        rand_float = random.uniform(LOWER_LIM, UPPER_LIM)
        time.sleep(rand_float)
    

if __name__ == "__main__":
    main()