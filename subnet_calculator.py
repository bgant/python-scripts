#!/usr/bin/python3
#
# Brandon Gant
# 11/03/2019
#
# Wanted to see if I have learned enough Python to write a Subnet Calculator

from sys import exit

def valid_ip():
    '''
    Asks you to enter an IP address and makes sure it is valid

    Returns a list of the four octets.
    '''

    IP_ERROR_MSG = 'Not a valid IP Address... each of the four numbers separated by a \'.\' can be 0 to 255'
    while True:
        ip = input('Enter IP Address:  ')
        if not ip:
            exit()  # Hit Enter without any text to exit program
        try:
            ip = ip.split('.')  # Split by '.' into list of strings
            ip = [int(n) for n in ip]  # Convert strings in list to integers
        except ValueError:
            print(IP_ERROR_MSG)
            continue
        if len(ip) != 4 or min(ip) < 0 or max(ip) > 255:  # Check for 4 octets and if any number is below zero or greater than 255
            print(IP_ERROR_MSG)
            continue
        break
    return ip


def valid_mask():
    '''
    Asks you to enter a Subnet Mask or CIDR notation and makes sure it is valid

    Returns a list of the four octets.
    '''

    while True:
        mask = input('Enter Subnet Mask or CIDR: ')
        if not mask:
            exit()  # Hit Enter without any text to exit program
        if '.' in mask:
            MASK_ERROR_MSG = 'Not a valid Subnet Mask... each of the four numbers separated by a \'.\' can be 0 to 255'
            try:
                mask = mask.split('.')  # Split by '.' into list of strings
                mask = [int(n) for n in mask]  # Convert strings in list to integers
            except ValueError:
                print(MASK_ERROR_MSG)
                continue
            if len(mask) != 4 or min(mask) < 0 or max(mask) > 255:  # Check for 4 octets and if any number is below zero or greater than 255
                print(MASK_ERROR_MSG)
                continue
            cidr = '{:b}'.format(mask[0]) + '{:b}'.format(mask[1]) + '{:b}'.format(mask[2]) + '{:b}'.format(mask[3])
            if int(cidr.lstrip('1'), 2) != 0:  # Strip all the beginning 1's, convert to integer, should equal zero if valid
                print('Not a valid Subnet Mask... Try entering CIDR notation with a value from 0 to 31')
                continue
            cidr = cidr.count('1')  # Count all the 1's to create CIDR notation
            print('(Subnet Mask {}.{}.{}.{} is CIDR {})'.format(mask[0], mask[1], mask[2], mask[3], cidr))
        else:
            CIDR_ERROR_MSG = 'Not valid CIDR notation... use values from 0 to 31'
            try:
                cidr = int(mask)
            except ValueError:
                print(CIDR_ERROR_MSG)
                continue
            if cidr < 0 or cidr > 31:  # Any number between 0 and 30 is valid, but will allow special case 31 which some routers recognize
                print(CIDR_ERROR_MSG)
                continue
            mask = ('1' * int(mask)) + ('0' * (32 - int(mask)))  # Convert CIDR number into string of 1's and 0's
            mask = [mask[0:8], mask[8:16], mask[16:24], mask[24:32]]  # Break single string into list of four 8-bit binary strings
            mask = [int(n, 2) for n in mask]  # Convert binary strings into integers
            print('(CIDR {} is Subnet Mask {}.{}.{}.{})'.format(cidr, mask[0], mask[1], mask[2], mask[3]))
        break
    return mask


def calc_cidr(mask):
    '''
    Returns CIDR notation of Subnet Mask

    Function input is a four octet list or tuple.
    i.e. calc_cidr([255, 255, 252, 0])
    '''

    cidr = '{:08b}'.format(mask[0]) + '{:08b}'.format(mask[1]) + '{:08b}'.format(mask[2]) + '{:08b}'.format(mask[3])
    cidr = int(cidr.count('1'))
    return cidr


def calc_network(ip, mask):
    '''
    Network = IP AND Subnet Mask

    Function input is the IP and Subnet Mask both in four octet lists or tuples.
    i.e. calc_network([192, 168, 0, 27], [255, 255, 255, 0])
    '''

    network = [ ip[x] & mask[x] for x in range(4)]  # Logical AND ('&') of each of the four values in ip and mask lists
    return network


def calc_flipped_mask(mask):
    '''
    Returns bit-flipped Subnet Mask

    Function input is the Subnet Mask in a four octet list or tuple.
    i.e. calc_flipped_mask([255, 255, 252, 0])
    '''

    mask_string = ['{:08b}'.format(mask[0]), '{:08b}'.format(mask[1]), '{:08b}'.format(mask[2]), '{:08b}'.format(mask[3])]  # Convert int to bin str
    flipped_mask = []  # Initialize empty list
    for item in mask_string:
        item = ''.join(['1' if x == '0' else '0' for x in item])  # Flip all the bits in the mask string to create flipped_mask
        flipped_mask.append(int(item, 2))  # Save the new flipped binary number strings as integers in a list
    return flipped_mask


def calc_broadcast(network, mask):
    '''
    Broadcast = Network OR bit-flipped Subnet Mask

    Function input is the Network and Subnet Mask both in four octet lists or tuples.
    i.e. calc_broadcast([192, 168, 2, 0], [255, 255, 255, 0])
    '''

    flipped_mask = calc_flipped_mask(mask)
    broadcast = [network[x] | flipped_mask[x] for x in range(4)]  # Logical OR ('|') of each of the four values in network and flipped_mask lists
    return broadcast


def calc_total_hosts(mask):
    '''
    Returns Total Hosts allowed on Subnet

    Function input is the Subnet Mask in four octet list or tuple.
    i.e. calc_total_hosts([255, 255, 255, 0])
    ''' 

    flipped_mask = calc_flipped_mask(mask) 
    flipped_mask = ('{:08b}'.format(flipped_mask[0]) + '{:08b}'.format(flipped_mask[1]) + '{:08b}'.format(flipped_mask[2]) + '{:08b}'.format(flipped_mask[3]))
    cidr = calc_cidr(mask)
    total_hosts =  int(flipped_mask, 2) - 1 if cidr != 31 else 1  # CIDR 31 is a special case
    return total_hosts


def main():
    while True:
        ######################################
        # Ask for IP and Subnet Mask (or CIDR)
        ######################################
        ip = valid_ip()
        mask = valid_mask()

        ###############################################
        # Calculate all values using IP and Subnet Mask
        ###############################################
        cidr = calc_cidr(mask)
        flipped_mask = calc_flipped_mask(mask)
        network = calc_network(ip, mask)
        broadcast = calc_broadcast(network, mask)
        total_hosts = calc_total_hosts(mask)

        ####################################
        # Display Calculated Network Numbers
        ####################################
        print()
        print('BINARY MATH:')
        print('{:08b}.{:08b}.{:08b}.{:08b} IP *AND*'.format(ip[0], ip[1], ip[2], ip[3]))
        print('{:08b}.{:08b}.{:08b}.{:08b} Subnet Mask'.format(mask[0], mask[1], mask[2], mask[3]))
        print('-' * 35)
        print('{:08b}.{:08b}.{:08b}.{:08b} Network *OR*'.format(network[0], network[1], network[2], network[3]))
        print('{:08b}.{:08b}.{:08b}.{:08b} Bit-Flipped Subnet Mask'.format(flipped_mask[0], flipped_mask[1], flipped_mask[2], flipped_mask[3]))
        print('-' * 35)
        print('{:08b}.{:08b}.{:08b}.{:08b} Broadcast'.format(broadcast[0], broadcast[1], broadcast[2], broadcast[3]))
        print()
        print('    Network: {}.{}.{}.{}/{}'.format(network[0],  network[1],   network[2],   network[3], cidr))
        print('Subnet Mask: {}.{}.{}.{}'.format(     mask[0],      mask[1],      mask[2],      mask[3]))
        print('   First IP: {}.{}.{}.{}'.format(  network[0],   network[1],   network[2],   network[3] + 1 if cidr != 31 else network[3]))  
        print('    Last IP: {}.{}.{}.{}'.format(broadcast[0], broadcast[1], broadcast[2], broadcast[3] - 1))
        print('  Broadcast: {}.{}.{}.{}'.format(broadcast[0], broadcast[1], broadcast[2], broadcast[3]))
        print()
        print('Total Number of Hosts: {:,}'.format(total_hosts))
        if cidr == 0: print('You control all IPv4 Internet Addresses?!?!')
        if cidr == 31: print('WARNING: CIDR 31 is a special case that will not work on all routers!')
        print()
        print('=' * 100)
        print()


if __name__ == '__main__':
    main()

