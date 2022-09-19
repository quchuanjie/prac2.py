"""
Replace the contents of this module docstring with your own details
Name:Quchuanjie
Date started:8/8/2022
GitHub URL:https://github.com/JCUS-CP1404/assignment-1---songs-quchuanjie.git
"""
from operator import itemgetter

choice_menu = " MENU:\n L = List Songs\n A = Add new songs\n C = Complete the song\n Q = Quit"
choice = ["l", "a", "c", "q"]


def main():

    print("Songs to Learn 1.0 - by Chuanjie Qu")
    take_songs = read_file()
    print(len(take_songs)," songs loaded")
    while True:
        print(choice_menu)
        menu_choice = input(">>>".lower())
        while menu_choice not in choice:
            print("Invalid menu choice")
            menu_choice = input(">>> ".lower())
        if menu_choice == "l":
            get_L(take_songs)
        elif menu_choice == "a":
            take_songs.append(get_A())
            take_songs.sort(key=itemgetter(1, 0))
        elif menu_choice == "c":
            get_C(take_songs, learn_song(take_songs))
        else:
            print(save_file(take_songs), "saved to song.csv")
            print("Have a Nice Day :)")
            exit()


def read_file():
    songs = []
    real = []
    open_file = open("songs.csv", "r")
    for i in open_file:
        songs.append(i.strip("\n"))

    for j in songs:
        real.append(j.split(','))
    real.sort(key=itemgetter(1, 0))
    open_file.close()
    return real


def get_L(take_songs):
    total = -1
    count = 0
    numbers = 0
    for e in take_songs:
        total += 1
        if e[3] == "u":
            count += 1
            print(total, ".  * {:40} - {:30} {:10} ({:<5})".format(e[0], e[1], " ", e[2]))
        else:
            numbers += 1
            print(total, ".    {:40} - {:30} {:10} ({:<5})".format(e[0], e[1], " ", e[2]))
    print(numbers, "songs learned,", count, "songs still to learn")


def learn_song(take_songs):
    for song in take_songs:
        if song[3] == "u":
            return False
    return True


def get_C(take_songs, learn_song):
    if learn_song is True:
        print("No more songs to learn!")
    else:
        print("Enter the number of a song to mark as learned")
        song_number = valid_int(">>> ")
        while song_number > len(take_songs) - 1 or song_number < 0:
            print("Invalid song number")
            song_number = valid_int(">>> ")
        if take_songs[song_number][3] == "u":
            take_songs[song_number][3] = "1"
            print(take_songs[song_number][0] + " by " + take_songs[song_number][1] + " Learned. ")
        elif take_songs[song_number][3] == "l":
            print("You have already learned ",take_songs[song_number][0])
    return take_songs


def get_A():
    add_new_song = []
    song_title = input("Title: ")
    while song_title == "":
        print("Input can not be blank")
        song_title = input("Title: ")
    add_new_song.append(song_title)

    song_artist = input("Artist: ")
    while song_artist == " ":
        print("Input can not be blank")
        song_artist = input("Artist: ")
    add_new_song.append(song_artist)

    song_year = valid_int(input("Year: "))
    while song_year <= 0:
        print("Number must be >= 0")
        song_year = valid_int(input("Year: "))
    add_new_song.append(str(song_year))
    add_new_song.append('u')
    print(song_title, "by", song_artist, "({})".format(song_year), "added to song list")
    return add_new_song


def valid_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid input; enter a valid number")


def save_file(take_songs):
    last_count = 0
    open_file = open("songs.csv", "w")
    for song in take_songs:
        open_file.writelines(','.join(song) + "\n")
        last_count += 1
    open_file.close()
    return last_count


if __name__ == '__main__':
    main()
