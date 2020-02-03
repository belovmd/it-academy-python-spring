def song_decoder(song):
    """Instructions

    Input:
    The input consists of a single non-empty string,
    consisting only of uppercase English letters,
    the string's length doesn't exceed 200 characters
    Output
    Return the words of the initial song that
    Polycarpus used to make a dubsteb remix (WUB). Separate
    the words with a space.
    Examples
    song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
    # =>  WE ARE THE CHAMPIONS MY FRIEND
    """
    list_of_words = song.split('WUB')
    return ' '.join(filter(lambda x: x != '', list_of_words))
    # return ' '.join([word for word in list_of_words if word])  Equal result


if __name__ == '__main__':
    input_song = input('Enter Sub Remix of song: ')
    print(song_decoder(input_song))
    # input test: WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB
