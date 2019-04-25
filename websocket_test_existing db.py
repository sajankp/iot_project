import json
import asyncio
import websockets
async def hello():
    async with websockets.connect('ws://35.244.13.244/ws/post') as websocket:
        value = int(input("what's the value "))
        await websocket.send(json.dumps({'temp':value}))
        greeting = await websocket.recv()
        return greeting
