<h1 align="center"> Documentation (VNgrok) </h1>
<p align="center">
    <a href="https://github.com/Vortex5Root/VNgrok/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Vortex5Root/VNgrok.svg" alt="License">
    <a href="https://github.com/Vortex5Root/VNgrok/releases"><img src="https://img.shields.io/github/downloads/Vortex5Root/VNgrok/total.svg" alt="GitHub all releases"></a><br>
    <a href="https://github.com/Vortex5Root/VNgrok/network"><img src="https://img.shields.io/github/forks/Vortex5Root/VNgrok.svg" alt="GitHub forks"></a>
    <a href="https://github.com/Vortex5Root/VNgrok/stargazers"><img src="https://img.shields.io/github/stars/Vortex5Root/VNgrok.svg" alt="GitHub stars"></a>
    <a href="https://github.com/Vortex5Root/VNgrok/watchers"><img src="https://img.shields.io/github/watchers/Vortex5Root/VNgrok.svg" alt="GitHub watchers"></a><br>
    <a href="https://github.com/Vortex5Root/VNgrok/issues"><img src="https://img.shields.io/github/issues/Vortex5Root/VNgrok.svg" alt="GitHub issues"></a>
    <a href="https://github.com/Vortex5Root/VNgrok/pulls"><img src="https://img.shields.io/github/issues-pr/Vortex5Root/VNgrok.svg" alt="GitHub pull requests"></a>
    <a href="https://github.com/Vortex5Root/VNgrok/commits/master"><img src="https://img.shields.io/github/last-commit/Vortex5Root/VNgrok.svg" alt="GitHub last commit"></a><br>
    <a href="https://github.com/Vortex5Root/VNgrok/releases"><img alt="Dynamic TOML Badge" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FVortex5Root%2FVNgrok%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAtFBMVEVHcEyWYTihdkuXYzrBjlqhbkHepWuzglG8hFGWYjmzglHepmz3z5iygVCWYjmWYjmxgVDsvorMlmDepmybaD2oe02ufU2leUzdpWqzglGfdUrgqnH616j%2F4LKWYjmvf1C3hVPepmyWYjmWZDuWYjmzglGWYjmwfk7fp22aZjz93a7VoGmpfFKdbEe4hlTFkFzwxZH30aDpuYO%2BnICUbUbGkl3jrnbjr3eSYjuuiWzNq4fjvI5PAatoAAAAJXRSTlMA4v34FBH4Jwwn4l8IXFG6%2FrWcv2PCZqdJxeX291Ci4uVQ5eQoZPLoqAAAAIxJREFUCNdFzscCgjAQBNA1JIAGVMDeW0iEAPb6%2F%2F9lCuqc9s1eBkDHpxTDN8E8mroJ9S1G0Sw7noSbrAMAHLvidshMERPwVlUuxF0Vb7ltgtdi5VUV%2BetcNAwZKyv%2BeP7J%2BD6VRaq5rKmiOUGoW3OzAzxEF2npLIgaGPbN1%2Bm07S4SjvkPOnjQI%2Bb4AGCaEYNClUKKAAAAAElFTkSuQmCC&label=Package%20Version"></a>
</p>

<h2 align="center">Introduction</h2>

> This is a program that creates a wrapper in the SSH tunnel function that allows you to host services without exposing your local ip address and also allows for you to switch ports without switching off your services.

| Problem | Solution |
| --- | --- |
| **Trying to expose your services in a way that you don't have to expose your local IP and changing ports without switching off your services** | **We solved this problem by creating a wrapper in the SSH tunnel function to allow to host services** |

<h2 align="center"> Index </h2>

| Topic | Sub-Topic |
| --- | --- |
| [Dependencies](#dependencies) | |
| [What Classes Are Available in vngrok](#what-classes-are-available-in-vngrok) | |
| | [Classes Index](#classes-index) |
| | [SSH Reverser Tunnel](#ssh-reverser-tunnel) |
| | [SSH Listener](#ssh-listener) |
| | [Reverse Tunnel Data](#reverse-tunnel-data) |
| [Aknowledgements](#aknowledgements) | |
| [Conclusion](#conclusion) | |

<h2 align="center">Dependencies</h2>

| Name | Version | Description |
| --- | --- | --- |
| [![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) | >=3.11 | Python is an interpreted high-level general-purpose programming language. |
| [pexpect](https://pexpect.readthedocs.io/en/stable/) | 4.8.0 | Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. |
| [pydantic](https://pydantic-docs.helpmanual.io/) | 1.8.2 | Data validation and settings management using python type annotations. |

<h2 align="center">What Classes Are Available in vngrok</h2>

<h3>Classes Index</h3>

| Class | Description |
| --- | --- |
| [![SSH_Reverser_Tunnel](https://img.shields.io/badge/SSH_Reverser_Tunnel-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](#ssh-reverser-tunnel) | This class is responsible for creating a new SSH tunnel. |
| [![SSH_Listener](https://img.shields.io/badge/SSH_Listener-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](#ssh-listener) | This class is responsible for listening to a new SSH tunnel. |
| [![Reverse Tunnel Data](https://img.shields.io/badge/ReverseTunnelData-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](#reverse-tunnel-data) | This class is responsible for storing the data of the reverse tunnel. |

<h3 align="center">SSH Reverser Tunnel</h3>

```python
from vngrok import SSH_Reverser_Tunnel

# Create a new SSH_Reverser_Tunnel
tunnel = SSH_Reverser_Tunnel(
    local_host="<local_host>", # The IP of the server that you want to expose to the internet.
    local_port=<local_port> : int, # The port of the server that you want to expose to the internet.
    remote_port=<remote_port> : int, # The remote port is the port responsible to host your server locally on the remote host.
    listening_host="<listening_host>", # The listening host is the IP that you want to listen to receive connections.
    listening_port=<listening_port> : int, # The listening port is the port that you want to receive connections.
)
```

<h3 align="center">SSH Listener</h3>

```python
from vngrok import SSH_Listener

# Create a new SSH_Listener
listener = SSH_Listener(
    listening_host="<listening_host>", # The IP that you want to listen to receive connections.
    listening_port=<listening_port> : int, # The port that you want to receive connections.
    local_port=<local_port> : int, # The port of the server that you want to expose to the internet.
    password="<password>", # The password of the server that you want to expose to the internet.
)
```

<h3 align="center">Reverse Tunnel Data</h3>

```python
from vngrok import ReverseTunnelData

# Create a new ReverseTunnelData
data = ReverseTunnelData(
    local_host="<local_host>", # The IP of the server that you want to expose to the internet.
    local_port=<local_port> : int, # The port of the server that you want to expose to the internet.
    remote_port=<remote_port> : int, # The remote port is the port responsible to host your server locally on the remote host.
    listening_host="<listening_host>", # The IP that you want to listen to receive connections.
    listening_port=<listening_port> : int, # The port that you want to receive connections.
)
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
