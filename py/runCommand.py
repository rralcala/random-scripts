#!/usr/bin/env python
"""
	Multiple Host command issuer.
	This tool read from stdin a list of hosts and ssh to them to run uptime. This assumes that all the hosts are in the known_hosts file and
	we can login to them using key exchange (so there is no need for user interaction during the authentication).
	
	Run with -s to put all the output in one file, or without arguments to have several host.out files. The first will be faster because we
	only write and create one file.
	@author: Roberto Rodriguez <rralcala@gmail.com>
"""

import threading
import subprocess
import time
import sys
import Queue

# Define 2 queues: one for ssh tasks, and one for output writing (only one thread because uptime gives shot output)
hosts_queue = Queue.Queue()
out_queue = Queue.Queue()

# Use 32 threads to issue the commands, because we assumed that we have 8 cpus, so we allow 3 processes to wait for data while 1 is running)
threads = 32;
start = time.time()
single = False

if '-s' in sys.argv[1:]:
	single = True

# THis is the writer thread
class ThreadWrite(threading.Thread):
        def __init__(self, out_queue, file):
                threading.Thread.__init__(self)
                self.out_queue = out_queue
		self.file = file

        def run(self):
                while True:
			# Get write jobs from the queue, one job is a host output pair
                        host, out = self.out_queue.get()
			if self.file is None:
				# If -s is not set write them to its own file
                        	f = open(host+'.out', 'a')
				f.write(out)
				f.close()
			else:
				#If -s is set write them to the output file, previously opened.
				self.file.write(host + ': ' + out)
			# flag the job as done
			self.out_queue.task_done()

#This is the command runner, for each entry in stdin it executes ssh VALUE uptime
class ThreadRunCommand(threading.Thread):
	def __init__(self, hosts_queue, out_queue):
		threading.Thread.__init__(self)
		self.hosts_queue = hosts_queue
        	self.out_queue = out_queue
          
	def run(self):
		while True:
			# Get a host from the queue
			host = self.hosts_queue.get()
			# Run ssh as mentiones earlier
			proc = subprocess.Popen(["ssh",host,"uptime"], stdout=subprocess.PIPE)
			(out, err) = proc.communicate()
			# create a new write job and flag the host as processed.
			self.out_queue.put([host, out])
			self.hosts_queue.task_done()

def main(single):
	# Read the hosts from stdin, they should be in user@host format
	hosts=sys.stdin.read().split()
	# Queue them for processing
	for h in hosts:	
		hosts_queue.put(h)
	# Start the 32 worker threads
	for j in range(threads):
		t = ThreadRunCommand(hosts_queue, out_queue)
		t.daemon = True
		t.start()
        # Open the output file if we're working in single output mode
	if single:
		file = open('output', 'w')
	else:
		file = None
	# Start the Writer thread
	tW = ThreadWrite(out_queue, file)
        tW.daemon = True
        tW.start()
	# Wait for the jobs to finnish.
	hosts_queue.join()
	out_queue.join()
main(single)
# Show in stdout the the time it took to issue all the commands
print "Elapsed Time: %s" % (time.time() - start)
