# 1 --------------------------------------------------------------------------
# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
# покупка билета в транспортной компании, или простая РПГ.
# Создайте несколько объектов классов, которые описывают ситуацию
# Объекты должны содержать как атрибуты так и методы класса для
# симуляции различных действий. Программа должна инстанцировать
# объекты и эмулировать какую-либо ситуацию - вызывать методы,
# взаимодействие объектов и т.д.

# My model describe train with 3 types of wagons:
#  1. general  - общий
#  2. reserved seat - плацкартный
#  3. compartment - купейный
# I'm forming a train from wagons and buy tickets for passenger.

class Passenger:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return '{} {}, ID: {}'.format(self.first_name,
                                      self.last_name,
                                      self.id_number)


class Ticket:
    def __init__(self, passenger, train, wagon, seat):
        self.passenger = passenger
        self.train = train
        self.wagon = wagon
        self.seat = seat

    def __str__(self):
        return 'Ticket: {}, wagon {}, seat {} - {}'.format(
            self.train,
            self.wagon,
            self.seat,
            self.passenger
        )


class Wagon:
    def __init__(self, type_wagon='general'):
        self.seats = []
        self.type_wagon = type_wagon
        if type_wagon == 'compartment':
            self.free_seats = 36
        elif type_wagon == 'reserved':
            self.free_seats = 54
        else:
            self.free_seats = 81


class Train:
    def __init__(self, number, poin_from, point_to, departure):
        self.wagons = []
        self.number_train = number
        self.point_from = poin_from
        self.point_to = point_to
        self.departure = departure

    def add_wagon(self, type_wagon):
        self.wagons.append(Wagon(type_wagon))

    def del_wagon(self):
        if self.wagons:
            return self.wagons.pop()

    def made_wagons(self, general, reserved, compartment):
        for _ in range(compartment):
            self.add_wagon('compartment')
        for _ in range(reserved):
            self.add_wagon('reserved')
        for _ in range(general):
            self.add_wagon('general')

    def buy_ticket(self, passenger, type_wagon):
        for n_wagon, wagon in enumerate(self.wagons):
            if type_wagon == wagon.type_wagon and wagon.free_seats > 0:
                wagon.free_seats -= 1
                wagon.seats.append(passenger)
                return Ticket(passenger, self, n_wagon + 1,
                              len(wagon.seats))
        return None

    def __str__(self):
        return 'train № {}, {} - {}, departure: {}'.format(self.number_train,
                                                           self.point_from,
                                                           self.point_to,
                                                           self.departure)


my_train = Train(723, 'Minsk', 'Brest', '7:00')
# 3 - общих, 5 - плацкартных, 2 - купейных
my_train.made_wagons(3, 5, 2)
print(my_train)

Iam = Passenger('Ruslan', 'Mazouka', 'B2342334346B190')
ticket = my_train.buy_ticket(Iam, 'compartment')
if ticket:
    print(ticket)
    assert ticket.__str__() == ("Ticket: train № 723, Minsk - Brest,"
                                " departure: 7:00,"
                                " wagon 1, seat 1 - Ruslan Mazouka,"
                                " ID: B2342334346B190")
Iam = Passenger('Ivan', 'Petrov', 'P233445753646B190')
ticket = my_train.buy_ticket(Iam, 'reserved')
if ticket:
    print(ticket)
