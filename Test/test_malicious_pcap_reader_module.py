#Initial Basic Test -Assure proper pcap reading of the example/maliciousTraffic.pcap
import sys

print sys.path[0]
if sys.path[0]:
	sys.path.insert(0, sys.path[0]+'/../Source/Module/')
else:
	sys.path.insert(0,'/../Source/Module/')

import pcapReader
def test_malicious_packets_to_be_read():
	# Reading malicious capture traffic
	maliciouspcapfile = pcapReader.pcapReader(sys.path[0]+'examples/maliciousTraffic.pcap')
	# Checking if the packet db is created without any hassle
	if maliciouspcapfile.packetDB:
		assert True


test_malicious_packets_to_be_read()
