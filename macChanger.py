import subprocess as sp

sp.call("sudo","ipconfig","OAM-016721","down")
sp.call("sudo","ipconfig","OAM-016721","hw","name","00:11:22:33:44:55")
sp.call("sudo","ipconfig","OAM-016721","up")

