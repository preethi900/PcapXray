 #Initial Basic Test - Assure proper device details reading of the examples/test.pcap
import sys
print sys.path[0]
if sys.path[0]:
    sys.path.insert(0, sys.path[0]+'/../Source/Module/')
else:
    sys.path.insert(0,'/../Source/Module/')

import pcapReader
import deviceDetailsFetch
def test_device_details_to_be_read():
    pcapfile = pcapReader.pcapReader(sys.path[0]+('/examples/test.pcap')
    for ip in pcapfilei.packetDB:
        macObj = deviceDetailsFetch(pcapfile.packetDB[ip])

test_device_details_to_be_read()
