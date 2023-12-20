import time
import emulator

ld = emulator.LDPlayer(ldplayer_dir='F:/LDPlayer/LDPlayer9')
# print(ld.emulators)


em = ld.emulators [6] 
em.start ()
time.sleep(10)
# em.run_app(package_name="com.facebook.katanb")


packages = em.list_packages()

print(packages)