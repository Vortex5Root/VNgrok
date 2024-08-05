<h1 align="center">Load Balancer SSHTunnel (cli_exempla.py)</h1>
<p align="center">
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="License">
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/releases"><img src="https://img.shields.io/github/downloads/Vortex5Root/Loadbalancer-SSHTunnel/total.svg" alt="GitHub all releases"></a><br>
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/network"><img src="https://img.shields.io/github/forks/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="GitHub forks"></a>
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/stargazers"><img src="https://img.shields.io/github/stars/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="GitHub stars"></a>
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/watchers"><img src="https://img.shields.io/github/watchers/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="GitHub watchers"></a><br>
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/issues"><img src="https://img.shields.io/github/issues/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="GitHub issues"></a>
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/pulls"><img src="https://img.shields.io/github/issues-pr/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="GitHub pull requests"></a>
    <a href="https://github.com/Vortex5Root/Loadbalancer-SSHTunnel/commits/master"><img src="https://img.shields.io/github/last-commit/Vortex5Root/Loadbalancer-SSHTunnel.svg" alt="GitHub last commit"></a>
</p>
<h2 align="center">How To Use</h2>


2. After you do the above commands run the Tunnel:

```bash
cd ssh_tunnel && python3 __init__.py
```

3. After you run the Tunnel you are going to be prompted of what commands you want to run this are the following options:

<h3 align="center">To start a new tunnel use</h3>

```bash
$> new <local_host> <local_port> <remote_port> <listening_host> <listening_port>
```

Note:
- **<local_host>**: The IP of the server that you want to expose to the internet.
- **<local_port>**: The port of the server that you want to expose to the internet.
- **<remote_port>**: The remote port is the port responsible to host your server locally on the remote host.
- **<listening_host>**: The listening host is the IP that you want to listen to receive connections.
- **<listening_port>**: The listening port is the port that you want to receive connections.

<h3 align="center">To stop the Tunnel run this command</h3>

```bash
$> stop <remote_port>
```

<h3 align="center">To list all the open tunnels run</h3>

```bash
$> list
```

<h3 align="center">To exit the program run</h3>

```bash
$> exit 
```

<h2 align="center">Aknowledgements</h2>

<p align="center">
    <br>[Coder]<br>
    <a href="https://github.com/Vortex5Root"><img src=https://avatars.githubusercontent.com/u/102427260?s=200&v=4 width=50 style="border-radius: 50%;"><br>Vortex5Root <br><b>        {Full-Stack Software Engineer}</b></a><br>
    <br>[Contributor]<br>
    <a href="https://github.com/PandemicOfNukes"><img src=https://avatars.githubusercontent.com/u/59929476?s=200&v=4 width=50 style="border-radius: 50%;"><br>PandemicOfNukes <br><b>        {Student}</b></a><br><br>
</p>

<h2 align="center">Conclusion</h2>
As you can see, we made an efficient to create a wrapper in the SSH tunnel function that allows you to create your services without exposing yourself and allows the administrator to switch ports with no downtime.
