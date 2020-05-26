import multiprocessing as mp
import time

import colorama

colorama.init(autoreset=True)

nwc = colorama.Fore.BLUE
mcc = colorama.Fore.BLACK

def cpu_intensive_task():
    for _ in range(1, 300_000_000):
         pass

def nisus_wettus():
    cpu_intensive_task()
    time.sleep(0.0005)
    print(nwc + "Crucifixion?")
    print(nwc + "What?")
    print(nwc + "Oh, oh that´s jolly good well. Off you go then.")
    print(nwc + "[laughing] Oh, I see, very good. Well...")

def mr_cheeky():
    cpu_intensive_task()
    print(mcc + "Ah, no. Freedom.")
    print(mcc + "Eh, freedom for me. They said I hadn't done anything, so I can go free and live on an island somewhere.")
    print(mcc + "No, I'm only pulling your leg, it's crucifixion really!")
    print(mcc + "Yes I know, out the door, one cross each, line on the left.")

def main():
    nw = mp.Process(target=nisus_wettus)
    mc = mp.Process(target=mr_cheeky)
    nw.start()
    mc.start()
    nw.join()
    mc.join()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'time elapsed: {end-start}')