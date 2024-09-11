from socket import *
import subprocess

sName = "127.0.0.1"
sPort = 65431

with socket(AF_INET, SOCK_STREAM) as sSocket:
	sSocket.bind((sName, sPort))
	sSocket.listen(1)
	print("Server is readu to receive")
	
	while True:
		connSocket, addr = sSocket.accept()
		
		while True:
			request = connSocket.recv(1024).decode()
			print(f"Received the request:\n{request}")
			
			if request == "exit":
				connSocket.send("Session is terminated".encode())
				break
			
			status, output = subprocess.getstatusoutput(request)
			response = output if status == 0 else f"Error:{output}"
			connSocket.send(response.encode())
			
		print("Bye")
		connSocket.close()
