import asyncio

class CrucifixionLineProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        transport.write("Next. Crucifixion?\n".encode())

    def data_received(self, data):
        answer = data.decode().rstrip().lower()
        if answer == "ah, no. freedom.":
            self.transport.write("What?\nOh. Oh, well, that's jolly good. Well, off you go, then.\n".encode())
            self.transport.close()
        elif answer.startswith("yes"):
            self.transport.write("Good. Out of the door. Line on the left. One cross each.\n".encode())
        else:
            self.transport.write("Hmm. Out of the door. Line on the left. One cross each.\n".encode())
        self.transport.write("Next. Crucifixion?\n".encode())

async def main():
    eventloop = asyncio.get_running_loop()

    server = await eventloop.create_server(lambda: CrucifixionLineProtocol(), '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())