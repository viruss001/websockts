# Importing the relevant libraries
import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    try:
        # Connect to the server
        async with websockets.connect(url) as ws:
            # Send a greeting message
            await ws.send("Hello Server!")
            # Stay alive, listening to incoming messages
            while True:
                try:
                    msg = await ws.recv()
                    print(msg)
                except websockets.exceptions.ConnectionClosedError as e:
                    print(f"Connection closed: {e}")
                    break
    except Exception as e:
        print(f"Error connecting to the server: {e}")

# Start the connection
asyncio.run(listen())
