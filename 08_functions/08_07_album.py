# Timothy Vaculik
# Making albums
# I think is is difficulty of 4/10

def make_album(artist_name, album_title, number_of_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

album1 = make_album('Taylor Swift', '1989')
print(album1)

album2 = make_album('Ed Sheeran', 'Divide', 12)
print(album2)

album3 = make_album('Adele', '25')
print(album3)