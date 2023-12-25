import emulator
import threading
import random
ld = emulator.LDPlayer(ldplayer_dir='F:/LDPlayer/LDPlayer9')
# print(ld.emulators)


def open_emulator(index):
    em = ld.emulators[index]
    em.start()
    em.wait_to_started()
    ld.sort_window()



    i = 4
    while i < 9:

        RandomLike = [1,2,3,4,5,6,7,8,9,0]

        getApp = open('Packge/app.txt', 'r')
        App = getApp.readlines()
        FacebookApp = App[i]
        i += 1

        em.run_app(package_name=FacebookApp)
        em.wait(10)

#scrool

        # for scroll in range(random.randint(3,4)):
        #     em.swipe(_from=(211, 703), to=(207, 262),duration=random.randint(150,300))      # Scroll
        #     Like = random.choice(RandomLike)       # Random Like 
        #     if  Like == 0 or Like == 5 or Like == 9:
        #         em.wait(random.randint(3,6))         # Sleep before like
        #         try:
        #             em.tap_to_img(img_path="img/btnLike.png", timeout=0, threshold=0.8)       #Click Image Like
        #             em.wait(random.randint(3,6))         # Sleep after like
        #         except:pass
        #     else:
        #         em.wait(random.randint(3,7)) # if min like sleep
        # em.back()
        # em.wait(8)

# Check-in

        try:
            em.tap_to_img(img_path="img/check_in/1.png", timeout=0, threshold=0.8)
            em.wait(5)

            em.tap_to_img(img_path="img/check_in/2.png", timeout=0, threshold=0.8)
            em.wait(7)

            em.tap_to_img(img_path="img/check_in/3.png", timeout=0, threshold=0.8)
            em.wait(8)

            em.tap((176, 336))
            em.wait(5)

            try:
                em.tap_to_img(img_path="img/check_in/4.png", timeout=0, threshold=0.8)
                em.wait(8)

                em.tap_to_img(img_path="img/check_in/5.png", timeout=0, threshold=0.8)
                em.wait(8)
            except:
                em.tap_to_img(img_path="img/check_in/6.png", timeout=0, threshold=0.8)
                em.wait(8) 
            pass

        except:pass






        




indices_to_open = [7]


threads = []
for index in indices_to_open:
    thread = threading.Thread(target=open_emulator, args=(index,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()




