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
    print(mcc + "Eh, freedom for me. They said I hadn't done anything, so I can go free and live on an island somewhere.")
    await cue()
    print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
    await cue()
    print(mcc + "Yes I know, out the door, one cross each, line on the left.")

class Scene:
    def __init__(self):
        self.cues = []

    def ready(self, actor):
        self.cues.append(actor)

    def action(self):
        while len(self.cues) > 0:
            actor = self.cues.pop(0)
            try:
                actor.send(None)
                self.cues.append(actor)
            except StopIteration:
                pass

def main():
    scene = Scene()
    scene.ready(nisus_wettus())
    scene.ready(mr_cheeky())
    scene.action()


if __name__ == '__main__':
    main()
