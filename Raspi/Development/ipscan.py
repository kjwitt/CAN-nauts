import sh


print "Scanning..."
conn=0
for addr in range(2,10):
	ipaddr = "192.168.1." + str(addr)
	
	try:
		sh.ping(ipaddr, "-c 1 -s 11 -q", _out="/dev/null")
		print "Ping to:",ipaddr,"OK"
		conn+=1
	except:
		print "No response from:",ipaddr
print "Number of devices connected:",conn			
