from socket import *
import time

mGroup = ("224.0.0.1", 4321)

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 16)

while True:
	msg = input("Enter the message for multicast: ")
	print("Sending message")
	sockfd.sendto(msg.encode(), mGroup)
	time.sleep(1)
