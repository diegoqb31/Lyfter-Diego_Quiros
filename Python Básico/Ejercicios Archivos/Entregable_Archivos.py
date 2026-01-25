def open_and_save_file(path):
    list_of_songs = []
    with open(path, encoding='utf-8') as file:
        for line in file.readlines():
            list_of_songs.append(line)
    return list_of_songs


def write_songs_file(path, list_of_songs):
    with open(path, 'w', encoding='utf-8') as file:
        for song in list_of_songs:
            file.write(song)


def process_songs(input_path, output_path):
    try:
        songs = open_and_save_file(input_path)
        write_songs_file(output_path, songs)
    except OSError as error:
        print(f"Ha ocurrido un error: {error}")


process_songs('Songs.txt', 'Songs_list_result.txt')