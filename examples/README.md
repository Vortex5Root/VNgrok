<h1 align="center">VNgrok (cli_exempla.py)</h1>
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

> This Exempla is a program how use vngronk to create a cli to integrate Load-Balancer-SSHTunnel in your project.

<h2 align="center">Index</h2>

| Topic | Sub-Topic |
| --- | --- |
| [Introduction](#introduction) | |
| [Dependencies](#dependencies) | |
| [How to Test cli_exempla](#how-to-test-cli_exempla) | |
| [How to use the cli?](#how-to-use-the-cli) | |
| [Aknowledgements](#aknowledgements) | |
| [Conclusion](#conclusion) | |


<h2 align="center">How to Test cli_exempla</h2>

1. First you need to install the dependencies:

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
```bash
poetry init # To create a new project
poetry shell # To start the shell
poetry add git+https://github.com/Vortex5Root/VNgrok.git
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
```bash
pip install git+https://github.com/Vortex5Root/VNgrok.git#egg=vngrok
```

2. After you do the above commands run the Tunnel:

```bash
cd examples
```

3. Run the following command:

```bash
python cli_exempla.py
```

3.1. Help Menu:

```bash
SSH Reverser Tunnel

options:
  -h, --help            show this help message and exit
  --remote_host REMOTE_HOST
                        Remote host
  --remote_port REMOTE_PORT
                        Remote port
  --user USER           User
  --password PASSWORD   Password
```

4. Run the following command:

```bash
python cli_exempla.py --remote_host <remote_host> --remote_port <remote_port> --user <user> --password <password>
```

<h2 align="center">How to use the cli?</h2>

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
