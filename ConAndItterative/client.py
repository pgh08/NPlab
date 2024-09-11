from socket import *
port = 4444

cSocket = socket(AF_INET, SOCK_STREAM)

try:
	cSocket.connect(("127.0.0.1", port))
	print("Connected to server \n")
	
	while True:
		data = cSocket.recv(1024)
		
		if not data:
			break
		
		print(f"Server : {data.decode()}")

except Exception as e:
	print(f"Error in connection : {e}")

finally:
	cSocket.close()
