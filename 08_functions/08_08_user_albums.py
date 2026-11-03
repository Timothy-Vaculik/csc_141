# Timothy Vaculik
# user albums with functions
# I think is is difficulty of 4/10

def make_album(artist_name, album_title, number_of_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

title_prompt = "\n What album are you thinking of? "
artist_prompt = "Who is the artist? "

print("\nEnter 'quit' at any time to quit.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)