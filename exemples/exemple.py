import time
from vngrok import SSH_Reverser_Tunnel, ReverseTunnelData

import argparse

def command_handler(command):
    args = command.split(" ")
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

def argument_parser():
    parser = argparse.ArgumentParser(description='SSH Reverser Tunnel')
    parser.add_argument('--remote_host', type=str, required=True, help='Remote host')
    parser.add_argument('--remote_port', type=int, required=True, help='Remote port')
    parser.add_argument('--user', type=str, required=True, help='User')
    parser.add_argument('--password', type=str, required=True, help='Password')
    return parser.parse_args()

if __name__ == "__main__":
    args = argument_parser()
    ssh_tunnel = SSH_Reverser_Tunnel(args.remote_host, args.remote_port, args.user, args.password)
    #tunnel_0 = ReverseTunnelData(local_host="192.168.1.130", local_port=8006, remote_port=20000, listening_host="41.216.182.128", listening_port=12001)
    while True:
        commnad = input("\nEnter command: ")
        if not command_handler(commnad):
            break
        time.sleep(1)
    del ssh_tunnel.tunnel_0