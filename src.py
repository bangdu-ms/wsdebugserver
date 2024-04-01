from websocket_server import WebsocketServer
from threading import Thread
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from datetime import datetime

# Called when client connects
def new_client(client, server):
	msg = "[%s] New client connected %s:%s" % (datetime.now(), client['address'][0], str(client['address'][1]))
	print(msg)
	server.send_message_to_all(msg)

# Called when a client sends msg to server
def _send_to_client(client, server):
    message = input()
    print (message)
    server.send_message(client,message)
    d = Thread(name='daemon', target=_send_to_client, args=[client, server])
    d.setDaemon = True
    d.start()

# Called when client disconnecting
def client_left(client, server):
	msg = "[%s] Client disconnected %s:%s" % (datetime.now(), client['address'][0], str(client['address'][1]))
	print(msg)

# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	msg = "[%s] Client(%s:%s) said: %s" % (datetime.now(), client['address'][0], str(client['address'][1]), message)
	print(msg)
	server.send_message_to_all(msg)

# Init args
parser = ArgumentParser("simple_websocket_server", formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--ip", help="IP address will be listened to", nargs='?', default="0.0.0.0", type=str)
parser.add_argument("-p", "--port", help="PORT will be listened to", nargs='?', default=8080, type=int)
args = parser.parse_args()

# Run server
print("[%s] Starting websocket server on %s:%s" % (datetime.now(), args.ip, args.port))
server = WebsocketServer(host = args.ip, port = args.port)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
