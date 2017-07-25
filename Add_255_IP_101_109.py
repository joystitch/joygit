from PySTAF import *
import sys
import threading
import time


def confip(ip,path1,path2):
    try:
        handle = STAFHandle("MyTest")
    except STAFException as e:
        print "Error registering with STAF, RC: %d" % e.rc
        sys.exit(e.rc)
    result = handle.submit(ip, "ping", "ping") # ping the destination machine
    if (result.rc != 0):
        print "Error submitting request, RC: %d, Result: %s" % (result.rc, result.result)
    request1 = 'START SHELL COMMAND %s' % str(path1) #start the first shell command on the destination machine
    result = handle.submit(ip, "process", request1)
    if (result.rc != 0):
        print "Error submitting request, RC: %d, Result: %s" % (result.rc, result.result)
    else:
        request2 = 'START SHELL COMMAND %s' % str(path2) #start the second shell command on the destination machine
        result = handle.submit(ip,"process",request2)
        print "Config %s Successfully \n" %(ip)

    rc = handle.unregister()
    sys.exit(rc)
	

		
threads = []
#i = 121
#ip ='192.168.80.%s' % str(i)
x1 = 81
path1 = 'C:/conf_ip_255_%s.bat' % str(x1)
x2 = x1 + 1 
path2 = 'C:/conf_ip_255_%s.bat' % str(x2)
for i in range(101,110): #Specifies the PCs which need to configure the IP
    ip ='192.168.80.%s' % str(i)
    n = "t%s = threading.Thread(target=confip, args=('%s', '%s', '%s'))" % (str(i), ip, path1, path2) #using multithreading
    exec(n)
    x1 = x2 + 1 #config the next command
    path1 = 'C:/conf_ip_255_%s.bat' % str(x1)
    x2 = x1 + 1 
    path2 = 'C:/conf_ip_255_%s.bat' % str(x2)
    m = "threads.append(t%s)" % str(i)
    exec (m)



for t in threads:
    t.setDaemon(True)
    t.start()

		
t.join()
time.sleep(1)

		


