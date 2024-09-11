from socket import *
import multiprocessing
port = 4444

def handle_client(cSocket, cAddr, cnt):
	print(f"Connection is received from {cAddr[0]} : {cAddr[1]}")
	print(f"Clients connected : {cnt} \n")
	cSocket.send(b"Hi client")
	cSocket.close()
	
def main():
	sockfd = socket(AF_INET, SOCK_STREAM)
	sockfd.bind(("127.0.0.1", port))
	sockfd.listen(10)
	
	print("Listening...\n")
	cnt = 0
	
	while True:
		cSocket, cAddr = sockfd.accept()
		cnt += 1
		process = multiprocessing.Process(target=handle_client, args=(cSocket, cAddr, cnt))
		process.start()
	
if __name__ == "__main__":
	main()
