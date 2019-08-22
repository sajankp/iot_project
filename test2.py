
import asyncio
import websockets
import websocket

@asyncio.coroutine
async def hello():
    uri = "ws://127.0.0.1/ws/post"
    async with websockets.connect(uri,host="127.0.0.1",port=8000,origin="ws://192.168.43.142") as websocket:
        name = input("What's your name? ")
        print(websocket.request_headers.keys)

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

# a=websocket.create_connection("ws://127.0.0.1:8000/ws/post")
# a.send("hi")
asyncio.get_event_loop().run_until_complete(hello())
# await hello()