# wsdebugserver
Simple websocket server for debugging. Use complied exe/binary file directly on Windows/Linux without installing

## How to use
* Copy exe/binary file to your websocket server OS and open it in command line(Use --help for detailed usage)
* Open client.html on your client browser, fill in your websocket server URL(ws://`websocketserverIP/URL`:`port`/`optionalpath`) and click connect
* After connected, send your customized msg to server by clicking send
* Toggle sending timestamp button to auto send current timestamp to web server per second. Useful for latency and stability test

## Known Support OS
Windows 11, WinServer 2019, CentOS7.9

## Limitation
Only Websocket is supported. HTTP is not and expectations are not captured currently.

If you are using it as backend server behind reverse proxy such as Azure Application Gateway, setup another http web server(IIS, nginx etc.) for health probe response(80 etc.), and use another port for websocket datapath traffic(8080 etc.) 

## Sample output

```
[root@VM03-CentOS websocket]# ./websocket_server 
[2024-04-01 01:50:29.229505] Starting websocket server on 0.0.0.0:8080
[2024-04-01 01:50:41.518432] New client connected 221.254.34.161:53530
[2024-04-01 01:50:43.991824] Client(221.254.34.161:53530) said: test
[2024-04-01 01:51:38.509527] Client disconnected 221.254.34.161:53530
```