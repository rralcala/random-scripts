#!/usr/bin/env python3
import threading
import subprocess
import time
import sys

plock = threading.Lock()
threads = 32


class ThreadUrl(threading.Thread):
	def __init__(self, hosts):
		threading.Thread.__init__(self)
		self.hosts = hosts

	def run(self):
		for h in self.hosts:
			proc = subprocess.Popen(["ssh", h, "uptime"], stdout=subprocess.PIPE)
			(out, err) = proc.communicate()
			plock.acquire()
			f = open(h+'.out', 'a')
			f.write(str(out))
			f.close()
			plock.release()


def main():
	hosts=sys.stdin.read().split()
	
	total = len(hosts);

	if total > threads:
		jobs = [ hosts[i*total // threads: (i+1)*total // threads] for i in range(threads) ]
	else:
		jobs = hosts		

	for j in jobs:
		t = ThreadUrl(j)
		t.daemon = False
		t.start()


if __name__ == '__main__':
	start = time.time()
	main()
	print("Elapsed Time: %s" % (time.time() - start))
