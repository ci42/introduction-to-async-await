import colorama

colorama.init(autoreset=True)

nwc = colorama.Fore.BLUE
mcc = colorama.Fore.BLACK

def nisus_wettus():
    print(nwc + "Crucifixion?")
    yield
    print(nwc + "What?")
    yield
    print(nwc + "Oh, oh that´s jolly good well. Off you go then.")
    yield
    print(nwc + "[laughing] Oh, I see, very good. Well...")

def mr_cheeky():
    print(mcc + "Ah, no. Freedom.")
    yield
    print(mcc + "Eh, freedom for me. They said I hadn't done anything, so I can go free and live on an island somewhere.")
    yield
    print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
    yield
    print(mcc + "Yes I know, out the door, one cross each, line on the left.")

def main():
    for _, _ in zip(nisus_wettus(), mr_cheeky()):
        pass

if __name__ == '__main__':
    main()

