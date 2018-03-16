import os

from subprocess import call


# call('mkdir sketchbooks',shell =True)
#change directory
# os.chdir('/home/qbc/PycharmProjects/ard/saved_/sketchbooks')
#call('touch readme.txt',shell= True)
# call('cp -a /usr/share/doc/arduino-mk/examples/Blink .',shell =True)
# os.chdir('/home/qbc/PycharmProjects/ard/saved_/sketchbooks/Blink')

os.chdir('/home/qbc/PycharmProjects/ard/sketchbooks/SW')


call('make',shell=True)
call("make upload",shell=True)
# #upload
# call('make',shell =True)
# call('make upload',shell =True)












