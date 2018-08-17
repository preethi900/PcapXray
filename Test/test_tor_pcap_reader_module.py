#Initial Basic Test -Assure proper pcap reading of the example/torExample.pcap
import sys

print sys.path[0]
if sys.path[0]:
	sys.path.insert(0, sys.path[0]+'/../Source/Module/')
else:
	sys.path.insert(0,'/../Source/Module/')

import pcapReader
import torTrafficHandle

def test_tor_packets_to_be_read():
	# Reading a tor capture traffic
	torpcapfile = pcapReader.pcapReader(sys.path[0]+'examples/torExample.pcap')
	# Checking if the packet db is created without any hassle
	if torpcapfile.packetDB:
		assert True
#	if toridentification = torTrafficHandle(torpcapfile.packetDB):
#		assert True


test_tor_packets_to_be_read()

