import threading
import time

import colorama

colorama.init(autoreset=True)

nwc = colorama.Fore.BLUE
mcc = colorama.Fore.BLACK

def cpu_consuming_task():
    for i in range(1, 300_000_000):
        pass

def nisus_wettus():
    cpu_consuming_task()
    print(nwc + "Crucifixion?")
    print(nwc + "What?")
    print(nwc + "Oh, oh that´s jolly good well. Off you go then.")
    print(nwc + "[laughing] Oh, I see, very good. Well...")

def mr_cheeky():
    cpu_consuming_task()
    print(mcc + "Ah, no. Freedom.")
    print(mcc + "Eh, freedom for me.They said I hadn't done anything, so I can go free and live on an island somewhere.")
    print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
    print(mcc + "Yes I know, out the door, one cross each, line on the left.")

def main():
    nw = threading.Thread(target=nisus_wettus, args=())
    mc = threading.Thread(target=mr_cheeky, args=())
    nw.start()
    mc.start()
    nw.join()
    mc.join()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(colorama.Fore.RED + f"time elapsed: {end - start}")