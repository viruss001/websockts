import websockets
import asyncio

PORT = 7890

print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            await websocket.send("Pong: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")

async def main():
    async with websockets.serve(echo, "localhost", PORT):
        print("Server started...")
        await asyncio.Future()  # Run forever

asyncio.run(main())
