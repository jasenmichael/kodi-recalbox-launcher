import os, time
import xbmcgui, xbmcaddon

__settings__  = xbmcaddon.Addon(id='script.recalbox.launcher')

dialog = xbmcgui.Dialog()
dialog.notification('Recalbox', 'Launching....', xbmcgui.NOTIFICATION_INFO, 5000)

time.sleep(1)

partition = int(__settings__.getSetting("partition"))

for soc in ('bcm2708','bcm2709','bcm2710'):
    os.system("sudo su -c 'echo %s > /sys/module/%s/parameters/reboot_part'" % (partition, soc))
    os.system("echo %s > /sys/module/%s/parameters/reboot_part" % (partition, soc))

os.system("sudo reboot %s || reboot %s || sudo reboot || reboot" % (partition, partition))