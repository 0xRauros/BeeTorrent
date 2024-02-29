# The heart of BeeTorrent ;)
import torrent
import utils
import sys
import bencodepy


def read_torrent_file(torrent_file_path):
    ''' Just read the content of the torrent file. '''
    try:
        with open(torrent_file_path, 'rb') as file:
            torrent_data = file.read()

        torrent_info = bencodepy.decode(torrent_data)
        print("Name of the file: ", torrent_info[b'info'][b'name'].decode('utf-8'))

    except FileNotFoundError:
        print(f"Error: The file '{torrent_file_path}' doesn't exist.")
    except IsADirectoryError:
        print(f"Error: '{torrent_file_path}' it's a directory, not a file.")
    except Exception as e:
        print(f"Error reading the torrent file: ", e)


def main():
    # check argument
    if len(sys.argv) != 2:
        print("Use: python client.py <file.torrent>")
        return

    torrent_file_path = sys.argv[1]

    read_torrent_file(torrent_file_path)

if __name__ == '__main__':
    main()