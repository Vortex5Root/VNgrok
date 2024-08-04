import socket
import threading
import time
from typing import Dict, List
from pydantic import BaseModel

from Functions import run_subprocess, start_logger

class ReverseTunnelData(BaseModel):
    local_host : str
    local_port : int
    remote_port : int
    listening_host : str
    listening_port : int


class SSH_Listener:
    def __init__(self,listening_host,listening_port,local_port,password):
        self.listening_host = listening_host
        self.listening_port = listening_port
        self.password = password
        self.local_port = local_port
        self.stop_event = threading.Event()
        self.thread = None

    def build_command(self):
        return f"sshpass -p '{self.password}' ssh -L {self.listening_host}:{self.listening_port}:localhost:{self.local_port} -N root@localhost"
    
    def start(self,host,port,username,password):
        command = self.build_command()
        command = f'sshpass -p "{password}" ssh -o StrictHostKeyChecking=no  -p {port} {username}@{host} "{command}"'
        self.thread = threading.Thread(target=run_subprocess, args=(command, self.stop_event))
        self.thread.start()
    

class SSH_Reverser_Tunnel:

    tunnels : Dict = {
        "in_used_ports": [],
        "tunnels": {}
    }

    def __init__(self, remote_host,remote_port,user,password) -> None:
        self.__dict__["logger"] = start_logger("ssh_reverser_tunnel.log")
        self.__dict__["remote_host"] = remote_host
        self.__dict__["remote_port"] = remote_port
        self.__dict__["user"] = user
        self.__dict__["password"] = password
        print("SSH_Reverser_Tunnel initialized.")

    def build_command(self, data : ReverseTunnelData) -> List[str]:
        command = f'sshpass -p "{self.password}" ssh -o StrictHostKeyChecking=no -R {data.remote_port}:{data.local_host}:{data.local_port} {self.user}@{self.remote_host} -p {self.remote_port}'
        #return ["sshpass","-p",f'"{self.password}"',"ssh","-o","PasswordAuthentication=yes", "-R", f"{data.remote_port}:{data.local_host}:{data.local_port}", f"{self.user}@{self.remote_host}", "-p", f"{self.remote_port}", "-vvv"]
        return command
    def __setattr__(self, name: str, value: ReverseTunnelData) -> None:
        data : ReverseTunnelData = value
        print("data",data)
        if data.remote_port not in self.tunnels["in_used_ports"]:
            command = self.build_command(data)
            stop_event = threading.Event()
            thread = threading.Thread(target=run_subprocess, args=(command, stop_event, self.password))
            remote_listening = SSH_Listener(data.listening_host, data.listening_port, data.remote_port, self.password)
            data_json = {
                "name": name,
                "thread": thread,
                "stop_event": stop_event,
                "local_host": data.local_host,
                "local_port": data.local_port,
                "remote_port": data.remote_port,
                "listening": remote_listening
            }
            thread.start()
            time.sleep(1)
            remote_listening.start(self.remote_host, self.remote_port, self.user, self.password)
            self.tunnels["tunnels"][data.remote_port] = data_json
            self.tunnels["in_used_ports"].append(data.remote_port)
            self.logger.info(f"Reverse tunnel started on port {data.remote_port}")
            self.__dict__[name] = data.remote_port
        else:
            self.logger.error(f"Port {data.remote_port} is already in use.")
            raise ValueError(f"Port {data.remote_port} is already in use.")
    
    def __delattr__(self, name: str) -> None:
        if name in self.__dict__:
            port = self.__dict__[name]
            data = self.tunnels["tunnels"][port]
            data["listening"].stop_event.set()
            data["stop_event"].set()
            #data["thread"].join()
            self.tunnels["in_used_ports"].remove(data["remote_port"])
            self.logger.info(f"Reverse tunnel stopped on port {data['remote_port']}")
            del self.tunnels["tunnels"][port]
            del self.__dict__[name]
        else:
            self.logger.error(f"Port {name} is not in use.")
            raise ValueError(f"Port {name} is not in use.")
    
    def __getattr__(self, name: str) -> None:
        if name in self.__dict__:
            port = self.__dict__[name]
            info = self.tunnels["tunnels"][port]
            return info
        else:
            self.logger.error(f"Port {name} is not in use.")
            raise ValueError(f"Port {name} is not in use.")

def command_handler(command):
    args = command.split(" ")
    print(args)
    if args[0] == "new":
        data = None
        try:
            data = ReverseTunnelData(local_host=args[1], local_port=int(args[2]), remote_port=int(args[3]), listening_host=args[4], listening_port=int(args[5]))
            ssh_tunnel.__setattr__(f"tunnel_{len(ssh_tunnel.tunnels['tunnels'])}", data)
        except Exception as e:
            print("user new <local_host> <local_port> <remote_port> <listening_host> <listening_port>")
    elif args[0] == "stop" and len(args) == 2:
        name = ssh_tunnel.tunnels["tunnels"][int(args[1])]["name"]
        ssh_tunnel.__delattr__(name)
    elif args[0] == "list":
        [print(f"{key}: {value}", end="\t\n") for key, value in ssh_tunnel.tunnels["tunnels"].items()]
    elif command == "exit":
        return False
    else:
        print("Command not found.")
    return True

def honey():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 17))
    server.listen(5)
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        client.send("Hello".encode())
        client.close()

def socket_c2():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 4444))
    server.listen(5)

if __name__ == "__main__":
    ssh_tunnel = SSH_Reverser_Tunnel("41.216.182.129", 22, "root", "M~yf*;?zF*v32Db")
    tunnel_0 = ReverseTunnelData(local_host="192.168.1.130", local_port=8006, remote_port=20000, listening_host="41.216.182.128", listening_port=12001)
    ssh_tunnel.tunnel_0 = tunnel_0
    while True:
        commnad = input("\nEnter command: ")
        if not command_handler(commnad):
            break
        time.sleep(1)
    del ssh_tunnel.tunnel_0
