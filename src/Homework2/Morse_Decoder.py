"""Morse Decoder

Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space
between each letter of each word. If the decrypted text starts with a
letter then you'll have to print this letter in uppercase.

Input: The secret message.

Output: The decrypted text.

Example:

morse_decoder("... --- -- .   - . -..- -") == "Some text"
morse_decoder("..--- ----- .---- ---..") == "2018"
morse_decoder(".. -   .-- .- ...   .-   --. "
              "--- --- -..   -.. .- -.--") == "It was a good day"

"""
MORSE = {'.-': 'a',
         '-...': 'b',
         '-.-.': 'c',
         '-..': 'd',
         '.': 'e',
         '..-.': 'f',
         '--.': 'g',
         '....': 'h',
         '..': 'i',
         '.---': 'j',
         '-.-': 'k',
         '.-..': 'l',
         '--': 'm',
         '-.': 'n',
         '---': 'o',
         '.--.': 'p',
         '--.-': 'q',
         '.-.': 'r',
         '...': 's',
         '-': 't',
         '..-': 'u',
         '...-': 'v',
         '.--': 'w',
         '-..-': 'x',
         '-.--': 'y',
         '--..': 'z',
         '-----': '0',
         '.----': '1',
         '..---': '2',
         '...--': '3',
         '....-': '4',
         '.....': '5',
         '-....': '6',
         '--...': '7',
         '---..': '8',
         '----.': '9'}


def morse_decoder(code):
    words_lst = code.split('   ')
    decode_lst = list()
    for word in words_lst:
        for char in word.split(' '):
            decode_lst.append(MORSE.get(char, ''))
        decode_lst.append(' ')
    decode_text = ''.join(decode_lst[:-1])
    return decode_text.capitalize() if code[0] != ' ' else decode_text


if __name__ == '__main__':
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"

    assert morse_decoder(
        ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    ) == "It was a good day"

    assert morse_decoder(
        "...- ...-- .-. -.--   .---- ----- -. --.   ... - "
        ".-. .---- -. --.   .-- .---- - ....   ... ----- -- "
        "...--   -. ..- -- -... ...-- .-. ....."
    ) == "V3ry 10ng str1ng w1th s0m3 numb3r5"
    print("All test passed!!!")
