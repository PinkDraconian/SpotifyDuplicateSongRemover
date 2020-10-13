import configparser
import spotify.sync as spotify


def main():
    parser = configparser.ConfigParser()
    parser.read('spotify.config')
    spotify_parser = parser['SPOTIFY']

    client_id = spotify_parser['client_id']
    client_secret = spotify_parser['client_secret']
    user_token = spotify_parser['user_id']
    playlist_uri = spotify_parser['playlist_uri']

    client = spotify.Client(client_id, client_secret)
    user = client.get_user(user_token)

    playlist = None
    for playlist in user.get_all_playlists():
        if playlist.uri == playlist_uri:
            break

    print('Found playlist {}'.format(playlist.name))

    tracks = []
    for track in playlist.get_all_tracks():
        track_tuple = (track.name, track.artist.name)
        if track_tuple in tracks:
            print('Duplicate track found: \'{}\' by \'{}\''.format(*track_tuple))
        else:
            tracks.append(track_tuple)

    client.close()


if __name__ == '__main__':
    main()
