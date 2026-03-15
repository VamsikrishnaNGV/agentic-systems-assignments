# WebSocket Echo Server using FastAPI
# Problem Statement
# Build a simple WebSocket-based chat echo server using FastAPI.

# Requirements
# Create a WebSocket endpoint at /ws.
# When a client connects, accept the WebSocket connection.
# The server should receive text messages from the client.
# For every message received, send back a response in the format:
# Server received: <message>
# Example:

# Client sends:

# Hello
# Server responds:

# Server received: Hello
# If the client disconnects, print the following message on the server:
# Client disconnected
# Testing the WebSocket
# You can test the WebSocket server using either the HTML client or the Python client given below.

# Option 1: Test using HTML
# Create a file named client.html and use the following code:

# <!DOCTYPE html>
# <html>
# <head>
#     <title>WebSocket Test</title>
# </head>
# <body>
#     <h2>WebSocket Echo Test</h2>

#     <input id="messageInput" type="text" placeholder="Enter message">
#     <button onclick="sendMessage()">Send</button>

#     <h3>Messages</h3>
#     <ul id="messages"></ul>

#     <script>
#         const ws = new WebSocket("ws://localhost:8000/ws");

#         ws.onmessage = function(event) {
#             const li = document.createElement("li");
#             li.textContent = event.data;
#             document.getElementById("messages").appendChild(li);
#         };

#         function sendMessage() {
#             const input = document.getElementById("messageInput");
#             ws.send(input.value);
#             input.value = "";
#         }
#     </script>
# </body>
# </html>
# Steps:

# Run the FastAPI server.
# Open client.html in a browser.
# Send messages and observe the responses.
# Option 2: Test using Python Client
# Install the required package:

# pip install websockets
# Create a file named client.py:

# import asyncio
# import websockets

# async def test():
#     async with websockets.connect("ws://localhost:8000/ws") as websocket:
#         await websocket.send("Hello Server")
#         response = await websocket.recv()
#         print(response)

# asyncio.run(test())
# Run the script:

# python client.py
# Expected output:

# Server received: Hello Server
from fastapi import FastAPI, WebSocket, WebSocketDisconnect


app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            message = await websocket.receive_text()

            await websocket.send_text(f"Server received: {message}")

    except WebSocketDisconnect:
        print("Client disconnected")
