import json
import asyncio
import websockets
async def hello(value):
    async with websockets.connect('ws://0.0.0.0:8000/ws/post') as websocket:
        # value = int(input("what's the value "))
        print(websocket)
        await websocket.send(json.dumps({'temp':value}))
        # greeting = await websocket.recv()
        # return greeting

# await hello(9)
asyncio.get_event_loop().run_until_complete((hello(23)))
asyncio.get_event_loop().run_forever()