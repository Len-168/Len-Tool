import emulator
import threading
import random
ld = emulator.LDPlayer(ldplayer_dir='F:/LDPlayer/LDPlayer9')
# print(ld.emulators)

OPENVPN = 0
ACTIVE = 1


def open_emulator(index):

    em = ld.emulators[index]

    em.start()
    em.wait_to_started()

    ld.sort_window()

    em.run_app(package_name='com.namecheap.vpn')
    em.wait(7)
    em.tap_to_img(img_path="img/ClickConnect.png", timeout=0, threshold=0.8)
    em.wait(7)
    

    i = 0
    while i < 9:
        
        RandomScroll = [15,20,25,30,35,40]
        RandomLike = [1,2,3,4,5,6,7,8,9,0]

        getApp = open('Packge/app.txt', 'r')
        App = getApp.readlines()
        FacebookApp = App[i]
        i += 1

        em.run_app(package_name=FacebookApp)
        em.wait(10)

        s_num = random.choice(RandomScroll)
        for scroll in range(s_num):
            em.swipe(_from=(211, 703), to=(207, 262),duration=random.randint(250,400))      # Scroll

            Like = random.choice(RandomLike)       # Random Like 
            if  Like == 0 or Like == 5 or Like == 9:
                em.wait(random.randint(3,5))         # Sleep before like
                try:
                    em.tap_to_img(img_path="img/btnLike.png", timeout=0, threshold=0.8)       #Click Image Like
                    em.wait(random.randint(3,5))         # Sleep after like
                except:pass
                
            else:
                em.wait(random.randint(3,7)) # if min like sleep


indices_to_open = [5,6,7,8,9]


threads = []
for index in indices_to_open:
    thread = threading.Thread(target=open_emulator, args=(index,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()




