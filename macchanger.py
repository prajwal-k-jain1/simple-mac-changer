#!/usr/bin/env python
import subprocess
import optparse
import re

def change_mac(interface,mac_adress):
    print("changing the macadress of " + interface + " to " + mac_adress)

    # subprocess.call('ifconfig '+interface +' down',shell=True)
    # subprocess.call('ifconfig '+interface+' hw ether '+mac_adress,shell=True)
    # subprocess.call('ifconfig '+interface+' up',shell=True)
    # subprocess.call('ifconfig',shell=True)

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_adress])
    subprocess.call(['ifconfig', interface, 'up'])
    subprocess.call(['ifconfig', interface])

def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to use')
    parser.add_option('-m', '--mac', dest='mac_adress', help='this option specifies the mac adress to be changed')
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] enter the interface ,use --help for more info")
    elif not options.mac_adress:
        parser.error("[-] enter the mac adress,use --help for more info")
    return options

def get_mac(interface):
    interface_result = subprocess.check_output(['ifconfig', interface])
    final_mac_result = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_result)
    if final_mac_result:
        return final_mac_result.group(0).decode('utf-8')
    else:
        print("[-] couldnt find the mac adress")


options=get_options()
current_mac = get_mac(options.interface)
print("current mac adress is:"+str(current_mac))
change_mac(options.interface,options.mac_adress)
current_mac= get_mac(options.interface)
if(current_mac==options.mac_adress):
    print("mac adress changed to "+current_mac)
else:
    print("mac adress hasnt been changed at all")