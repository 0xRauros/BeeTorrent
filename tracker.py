from utils import Utils

class Tracker:
    # torrent object instance previously created.
    def __init__(self, torrent):
        self.torrent = torrent

    def is_udp(self, tracker_url):
        ''' Chek if url is udp '''
        return tracker_url.startswith(b'udp://')

    def announce_to_trackers(self):
        all_trackers = self.torrent.get_all_trackers()
        for tracker_url in all_trackers:
            # UDP
            if self.is_udp(tracker_url):
                address, port = self.parse_udp_tracker_url(tracker_url)
                #todo
                request = self.build_udp_request()
                response = self.send_udp_request(address, port, request)
                peers = self.parse_udp_response(response)
                # handle the peers received by the tracker
            else:
                # HTTP
                pass


    def parse_udp_tracker_url(self, tracker_url):
        tracker_url = tracker_url[len(b'udp://'):]
        last_colon_index = tracker_url.rfind(b':')
        
        if last_colon_index == -1:
            raise ValueError(f"Url of tracker {tracker_url} is not valid.")
        
        address = tracker_url[:last_colon_index]
        # check if there is more data after the port.
        # example: :1337/announce -> we ignore it.
        slash_index = tracker_url.find(b'/')
        if slash_index == -1:
            port = tracker_url[last_colon_index + 1:]
        else: # hay /announce o su puta madre y algo más
            port = tracker_url[last_colon_index + 1:slash_index]

        return address, int(port)