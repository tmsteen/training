#!/bin/python3


def rotate_word(word, rotation_num):
    new_word = ''
    for i in word:
        position = ord(i) - 96 + rotation_num
        if position < 0:
            new_word += chr(ord('z') + position)
        else:
            new_word += chr(ord('a') + position - 1)

    print("The 'encrypted version of '{}' rotated by {} is: {}".format(
        word, rotation_num, new_word))


rotate_word('cheer', 7)
