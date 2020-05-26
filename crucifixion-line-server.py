import asyncio

async def crucifixion_line_handler(reader, writer):
    while True:
        writer.write("Next. Crucifixion?\n".encode())
        await writer.drain()
        response = await reader.readline()
        answer = response.decode().rstrip().lower()
        if answer == "ah, no. freedom.":
            writer.write("What?\nOh. Oh, well, that's jolly good. Well, off you go, then.\n".encode())
            break
        elif answer.startswith("yes"):
            writer.write("Good. Out of the door. Line on the left. One cross each.\n".encode())
        else:
            writer.write("Hmm. Out of the door. Line on the left. One cross each.\n".encode())
        await writer.drain()
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(crucifixion_line_handler, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())