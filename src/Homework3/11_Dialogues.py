"""Dialogues

Your task is to create a Chat class which could help a Human(name) and
Robot(serial_number) to make a conversation. This class should have a
few methods:
connect_human() - connects human to the chat.
connect_robot() - connects robot to the chat.
show_human_dialogue() - shows the dialog as the human sees it - as simple text.
show_robot_dialogue() - shows the dialog as the robot perceives it - as the
set of ones and zeroes. To simplify the task, just replace every vowel
('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and
special signs like ",", "!", etc.) with "1".
Dialog for the human should be displayed like this:
(human name) said: message text
(robot serial number): message text
For the robot:
(human name) said: 11100100011
(robot serial number) said: 100011100101
Interlocutors should have a send() method for sending messages to the dialog.
In this mission you could use the Mediator design pattern.

"""
from collections import deque


class Chat(object):
    VOWELS = "aeiouAEIOU"

    def __init__(self):
        self.human = None
        self.robot = None
        self.buffer = deque()

    def connect_human(self, human):
        self.human = human
        self.human.chat = self

    def connect_robot(self, robot):
        self.robot = robot
        self.robot.chat = self

    def show_human_dialogue(self):
        if self.human is not None:
            tmp_lst = list()
            for phrase in self.buffer:
                member, text = phrase
                tmp_lst.append(f'{member} said: {text}')
            return '\n'.join(tmp_lst)
        return ''

    def show_robot_dialogue(self):
        if self.robot is not None:
            tmp_lst = list()
            for phrase in self.buffer:
                member, text = phrase
                tmp_lst.append(f'{member} said: {self._trans_to_bin(text)}')
            return '\n'.join(tmp_lst)
        return ''

    @staticmethod
    def _trans_to_bin(dialog):
        for char in dialog:
            if char in Chat.VOWELS:
                dialog = dialog.replace(char, '0', 1)
            else:
                dialog = dialog.replace(char, '1', 1)
        return dialog


class Member(object):
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, text):
        if self.chat is not None:
            self.chat.buffer.append((self.name, text))
        else:
            print(f'{self.name} did not connect to chat')


class Human(Member):
    pass


class Robot(Member):
    pass


if __name__ == '__main__':
    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
    print("All tests passed!!!")

    chat_1 = Chat()
    maxim = Human('Max')
    robocop = Robot('Rob')
    chat_1.connect_human(maxim)
    chat_1.connect_robot(robocop)
    maxim.send('Google')
    maxim.send('It is cold')
    robocop.send('I do not understand you. I am machine')
    maxim.send("Don't worry!!! Be happy")
    assert chat_1.show_human_dialogue() == """Max said: Google
Max said: It is cold
Rob said: I do not understand you. I am machine
Max said: Don't worry!!! Be happy"""
