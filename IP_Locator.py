#This script checks if an IP is included in a network range in CIDR format
from ipaddress import ip_address, ip_network
print('What is the IP Address you would like to check?') #Asks for ip and saves to value
ipvalue = input()
print('What is the network range you would like to test?') #Asks for network range and saves to value
netrange1 = input()
print('Is there an additional range to test?') #Asks for additional network range and saves to separate value
answer = str.lower(input()) #negates capitalization
#NOTE: to add more network ranges beyond 2, a loop is required
if (answer == 'yes') or (answer == 'y'):
    print('Please enter the range.') #Asks for additional network range and saves to separate value
    netrange2 = input()
    subnet1 = ip_network(netrange1) #Variables for use in subnet action
    subnet2 = ip_network(netrange2)
    if subnet2.subnet_of(subnet1) == True: #Subnet action determines if second network range is subnet of first network range
        try:
            net = ip_network(netrange1)
            n2 = ip_network(netrange2)
            print(netrange2 + ' is a subnet of ' + netrange1) #Output when second network range is subnet of first network range
            if net.overlaps(n2) == True: #Overlap action determines if first network range overlaps second network range
                print(netrange1 + ' overlaps ' + netrange2 + ' in range ' + netrange2) #Output when networks overlap with range of overlap
            else:
                print(netrange1 + ' does not overlap ' + netrange2) #Null overlap output
            if(ip_address(ipvalue) in net) == True: #Condition for IP location
                print(ipvalue + ' is included in range.') #Output if IP is in range
            else:
                print(ipvalue + ' is not included in range.') #Null ip_address output
        except: #Error handling catchall
            print('An error occurred. Your IP input may be invalid.') #Error output
    elif subnet1.subnet_of(subnet2) == True: #Vice versa
        try:
            net = ip_network(netrange2)
            n1 = ip_network(netrange1)
            print(netrange1 + ' is a subnet of ' + netrange2)
            if net.overlaps(n1) == True:
                print(netrange2 + ' overlaps ' + netrange1 + ' in range ' + netrange1)
            else:
                print(netrange2 + ' does not overlap ' + netrange1)
            if(ip_address(ipvalue) in net) == True:
                print(ipvalue + ' is included in range.')
            else:
                print(ipvalue + ' is not included in range.')
        except:
            print('An error occurred. Your IP input may be invalid.')
    else:
        print('These network ranges are not related.') #Output for no subnet relation
else: #If no additional network range is input, the IP location is run using the ip_address action
    try:
        net = ip_network(netrange1)
        if(ip_address(ipvalue) in net) == True:
            print(ipvalue + ' is included in range.') #Output if IP is in range
        else:
            print(ipvalue + ' is not included in range.') #Null output
    except:
        print('An error occurred. Your IP input may be invalid.') #Error output


