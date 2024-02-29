# Functions and utilities needed for in different parts of the project.
import hashlib
import socket


class Utils:
    @staticmethod
    def send_udp_request(address, port, request):
        ''' Sends UDP request to an address and port. '''
        with socket.socket(socket.AF_INET, sock.SOCK_DGRAM) as sock:
            sock.sendto(request, (address, port))
            response, _ = sock.recvfrom(1024) # expected to 1024 bytes
        return response

    @staticmethod
    def receive_udp_response(sock, buffer_size):
        ''' Given a socket, get UDP response. '''
        pass

    @staticmethod
    def calculate_piece_hash(data):
        ''' Data must be a byte object '''
        sha1 = hashlib.sha1()
        sha1.update(data)
        return sha1.hexdigest()

    @staticmethod
    def bytes_to_kb(value):
        ''' kilobytes '''
        return value / 1024

    @staticmethod
    def bytes_to_mb(value):
        ''' megabytes '''
        return value / (1024 * 1024)