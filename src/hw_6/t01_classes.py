""" Party Invitations

As a model of my classes I decided to use task from ckeckio.org 'Party
Invitations': https://py.checkio.org/en/mission/party-invitations/

Each week you are meeting with your friends to spend some quality time
together. You want to simplify the process of gathering people and that's why
you've decided to write a program which could automate this process.

You should create the class Party(place) which will send the invites to all of
your friends. Also you should create the class Friend and each friend will be
an instance of this class.
Sometimes the circle of friends is changing - new friends appear, the old ones
disappear from your life (for example - move to another town).

In this mission you could use the Observer design pattern.
"""


class Friend:
    def __init__(self, name):
        self.name = name
        self._invite = 'No party...'

    def show_invite(self):
        return self._invite

    def set_invite(self, where_message):
        self._invite = where_message


class Party:
    def __init__(self, event):
        self._friends = set()
        self.event = event

    def add_friend(self, friend):
        self._friends.add(friend)

    def del_friend(self, friend_to_delete):
        if friend_to_delete in self._friends:
            self._friends.discard(friend_to_delete)

    def send_invites(self, where_message):
        for friend in self._friends:
            friend.set_invite(self.event + ': ' + where_message)


if __name__ == '__main__':
    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
