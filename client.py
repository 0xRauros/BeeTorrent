# The heart of BeeTorrent ;)
import torrent
import utils
import tracker

import sys
import bencodepy


def read_torrent_file(torrent_file_path):
    ''' Just read the content of the torrent file 
        and return the torrent data 
    '''
    try:
        with open(torrent_file_path, 'rb') as file:
            torrent_data = file.read()

        return torrent_data

    except FileNotFoundError:
        print(f"Error: The file '{torrent_file_path}' doesn't exist.")
        return
    except IsADirectoryError:
        print(f"Error: '{torrent_file_path}' it's a directory, not a file.")
        return
    except Exception as e:
        print(f"Error reading the torrent file: ", e)
        return


def print_art():
    art = '''
          __         .' '.
        _/__)        .   .       .
       (8|)_}}- .      .        .
        `\__)    '. . ' ' .  . '


    \033[33m\033[1mBee\033[0m\033[1mTorrent\033[0m

    Bittorrent client coded with \033[1m\033[34mPython\033[0m
        
    '''
    print(art)
def main():
    # check argument
    if len(sys.argv) != 2:
        print("Use: python client.py <file.torrent>")
        return

    torrent_file_path = sys.argv[1]

    torrent_data = read_torrent_file(torrent_file_path)
    
    # create torrent object
    new_torrent = torrent.Torrent(torrent_data)

    if new_torrent.is_single_file():
        print(new_torrent.pretty_info())
        
        new_tracker = tracker.Tracker(new_torrent)
        new_tracker.announce_to_trackers()


    else:
        print("We are sorry. BeeTorrent doesn't support multi files yest ;)")

if __name__ == '__main__':
    print_art()
    main()