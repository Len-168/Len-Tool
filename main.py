import time
import emulator
from emulator.node import By
import threading

ld = emulator.LDPlayer(ldplayer_dir='F:/LDPlayer/LDPlayer9')
# print(ld.emulators)

VPN = 0
ACTIVE = 1

 #  main function
def main():
    # function of threand
    def open_emulator(index):

        em = ld.emulators [index] 
        em.start ()
        em.wait(10)

        def vpnConnection():
            em.home()
            em.wait(4)
            openVPN = em.find_node(By.TEXT, "FastVPN")
            openVPN.tap()
            em.wait(4)

            vpnConnection = em.find_node(By.TEXT, "Connect VPN")
            vpnConnection.tap()
            em.wait(6)

        def startApp():
            i = 0
            while i < 10:
                i += 1
                em.home()
                openFacebook = em.find_node(By.TEXT,f"FB 0{i}")
                openFacebook.tap()

                em.wait(5)
                em.back()







    indices_to_open = [5,6]
    threads = []
    for index in indices_to_open:
        thread = threading.Thread(target=open_emulator, args=(index,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()



if __name__=="__main__": 
    main() 
