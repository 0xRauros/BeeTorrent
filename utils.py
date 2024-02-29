# Functions and utilities needed for in different parts of the project.
import hashlib

def send_udp_request(address, port, request):
    ''' Sends UDP request to an address and port. '''
    pass


def receive_udp_response(sock, buffer_size):
    ''' Given a socket, get UDP response. '''
    pass


def calculate_piece_hash(data):
    ''' Data must be a byte object '''
    sha1 = hashlib.sha1()
    sha1.update(data)
    return sha1.hexdigest()

