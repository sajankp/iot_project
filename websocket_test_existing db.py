import json

import websockets


async def hello():
    async with websockets.connect('ws://35.244.13.244/ws/post') as web_socket:
        value = int(input("what's the value "))
        await web_socket.send(json.dumps({'temp': value}))
        greeting = await web_socket.recv()
        return greeting
