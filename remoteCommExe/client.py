from socket import *

sName = "127.0.0.1"
sPort = 65431

with socket(AF_INET, SOCK_STREAM) as cSocket:
	cSocket.connect((sName, sPort))
	
	while True:
		command = input('Enter the command (or "exit" to quit):\n')
		
		if not command:
			print("Empty Command")
			continue
			
		cSocket.send(command.encode())
		response = cSocket.recv(1024).decode()
		print(f"From Server : \n {response}")
		
		if command == "exit":
			break
