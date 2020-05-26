import colorama

colorama.init(autoreset=True)

nwc = colorama.Fore.BLUE
mcc = colorama.Fore.BLACK

def nisus_wettus(callback):
    def first_cue(cb):
        print(nwc + "Crucifixion?")
        def second_cue(cb):
            print(nwc + "What?")
            def third_cue(cb):
                print(nwc + "Oh, oh that´s jolly good well. Off you go then.")
                def fourth_cue(cb):
                    print(nwc + "[laughing] Oh, I see, very good. Well...")
                    cb()
                cb(fourth_cue)
            cb(third_cue)
        cb(second_cue)
    first_cue(callback)

def mr_cheeky(callback):
    def first_cue(cb):
        print(mcc + "Ah, no. Freedom.")
        def second_cue(cb):
            print(mcc + "Eh, freedom for me. They said I hadn't done anything, so I can go free and live on an island somewhere.")
            def third_cue(cb):
                print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
                def fourth_cue():
                    print(mcc + "Yes I know, out the door, one cross each, line on the left.")
                cb(fourth_cue)
            cb(third_cue)
        cb(second_cue)
    first_cue(callback)

def main():
    nisus_wettus(mr_cheeky)

if __name__ == "__main__":
    main()