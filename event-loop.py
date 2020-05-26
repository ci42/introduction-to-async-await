import colorama

colorama.init(autoreset=True)

nwc = colorama.Fore.BLUE
mcc = colorama.Fore.BLACK

def cue():
    class Awaitable:
        def __await__(self):
            yield
    return Awaitable()

async def nisus_wettus():
    print(nwc + "Crucifixion?")
    await cue()
    print(nwc + "What?")
    await cue()
    print(nwc + "Oh, oh that´s jolly good well. Off you go then.")
    await cue()
    print(nwc + "[laughing] Oh, I see, very good. Well...")

async def mr_cheeky():
    print(mcc + "Ah, no. Freedom.")
    await cue()
    print(mcc + "Eh, freedom for me.They said I hadn't done anything, so I can go free and live on an island somewhere.")
    await cue()
    print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
    await cue()
    print(mcc + "Yes I know, out the door, one cross each, line on the left.")

class Eventloop:
    def __init__(self):
        self.queue = []

    def execute(self, task):
        self.queue.append(task)

    def run(self):
        while len(self.queue) > 0:
            task = self.queue.pop(0)
            try:
                task.send(None)
                self.queue.append(task)
            except StopIteration:
                pass

def main():
    eventloop = Eventloop()
    eventloop.execute(nisus_wettus())
    eventloop.execute(mr_cheeky())
    eventloop.run()

if __name__ == '__main__':
    main()
