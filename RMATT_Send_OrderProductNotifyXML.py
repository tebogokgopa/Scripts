
# ###################################################################
#Import required libraries
import atexit
import os
import sys
import tempfile
import time

sys.path.append(os.getenv('PYLIB_PATH'))


#######################################################################
#Handle security  and access issues

def abortScript():
    print("[!] Exit Handler called")
    if os.path.exists(config['LockFile']):
        os.remove(config['LockFile'])

def printException(exc_info):
    print('[!] EXCEPTION: \n  [0] %s\n  [1] %s\n [2] %s' %
          (exc_info[0], exc_info[1], exc_info[3] ))

def authenticateUser(employee_id,password,host_ip_address,computer_name):
    global security_user, security_functions_list, security_providers_list
    
    SSSi = SSSecurity_SessionInterface
    (security_user, security_functions_list, security_providers_list) = SSSi.startSession(
        employee_id, password, host_ip_address, computer_name)
    
# ####################################################################
  
    
# ####################################################################
#main function
def main():
    pass

if __name__ == '__main__':
    main()

