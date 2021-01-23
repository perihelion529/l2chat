# code for transmission and reception of L2 data
import sys
from scapy.all import srp,sendp
sendp("FFFFFFFF TESTING PAYLOAD plz don't murder me sysadmins", iface="ens33", loop=1, inter=0.02)
