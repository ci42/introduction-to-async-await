import colorama

colorama.init(autoreset=True)

nwc = colorama.Fore.BLUE
mcc = colorama.Fore.BLACK

def nisus_wettus():
    print(nwc + "Crucifixion?")
    print(nwc + "What?")
    print(nwc + "Oh, oh that´s jolly good well. Off you go then.")
    print(nwc + "[laughing] Oh, I see, very good. Well...")

def mr_cheeky():
    print(mcc + "Ah, no. Freedom.")
    print(mcc + "Eh, freedom for me. They said I hadn't done anything, so I can go free and live on an island somewhere.")
    print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
    print(mcc + "Yes I know, out the door, one cross each, line on the left.")

def main():
    nisus_wettus()
    mr_cheeky()

if __name__ == "__main__":
    main()