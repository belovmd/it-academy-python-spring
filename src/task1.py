# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
# покупка билета в транспортной компании, или простая РПГ. Создайте несколько
# объектов классов, которые описывают ситуацию Объекты должны содержать как
# атрибуты так и методы класса для симуляции различных действий. Программа
# должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать
# методы, взаимодействие объектов и т.д.


class Friend:
    def __init__(self, name):
        self.name = name
        self.info = 'No party...'

    def show_invite(self):
        return self.info


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = set()

    def add_friend(self, friend):
        self.friends.add(friend)

    def del_friend(self, friend):
        self.friends.remove(friend)

    def send_invites(self, info):
        for friend in self.friends:
            friend.info = '{}: {}'.format(self.place, info)


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
