# I handle the .torrent file info
import bencodepy
import hashlib

class Torrent:
    def __init__(self, torrent_data):
        '''
            Init the Torrent instance with the .torrent file data.
        '''
        self.torrent_data = torrent_data
        self.info = self.parse_torrent_file()
        self.info_hash = self.calculate_info_hash()

    # Define the methods needed to handle .torrent file data.

    def parse_torrent_file(self):
        return bencodepy.decode(self.torrent_data)

    def get_trackers(self):
        ''' if the dict doesn't contain announce-list 
            it should have announce.
            So we return it as a list.
        '''
        return self.info.get(b'announce-list', [self.info[b'announce']])

    
    def get_all_trackers(self):
        ''' Flat list of all trackers '''
        all_trackers = []
        for tracker_group in self.get_trackers():
            all_trackers.extend(tracker_group)
        return all_trackers


    def is_single_file(self):
        ''' Single file torrent or multi files '''
        return b'length' in self.info[b'info']

    def get_file_info(self):
        ''' Returns the file name and 
            size in a tuple (name, size) 
        '''
        # SINGLE FILE TORRENT
        if self.is_single_file():
            name = self.info[b'info'][b'name'].decode('utf-8')
            length = self.info[b'info'][b'length']
            return (name, length)

        # MULTIPLE FILE TORRENT (we don't support it yet)
        else:
            files = self.info[b'info'][b'files']
            return [(f[b'path'][0].decode('utf-8'), f[b'length']) for f in files]

    def calculate_info_hash(self):
        ''' Calculate the 'info' section of the torrent file. '''
        info_hash = hashlib.sha1(bencodepy.encode(self.info[b'info'])).hexdigest()
        return info_hash

    def validate_piece(self, piece_index, piece_data):
        ''' Check the integrity of a downloaded data piece comparing its hash
            with the one given in the torrent file.

            - piece_index: piece index we are validating in the torrent file
            - piece_data: downloaded piece content -> object bytes
        '''
        # caculate the hash of the downloaded piece
        piece_hash = hashlib.sha1(piece_data).digest() 
        # just the formula to get the part of the hash contained in info:pieces that corresponds to our
        # downloaded piece_hash. Check if they are same.
        valid = piece_data == self.info[b'info'][b'pieces'][piece_index*20:(piece_index+1)*20]
        return valid

    def pretty_info(self):
        pretty_info = ""
        pretty_info += f"File name: {self.get_file_info()[0]}\n"
        pretty_info += f"File size: {self.get_file_info()[1]} bytes\n"
        pretty_info += f"Trackers: \n"
        for tracker in self.get_all_trackers():
            pretty_info += f"   - {tracker.decode('utf-8')}\n"
        return pretty_info
