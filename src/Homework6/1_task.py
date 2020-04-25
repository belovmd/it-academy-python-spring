"""1 - models of real life

Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте несколько
объектов классов, которые описывают ситуацию Объекты должны содержать как
атрибуты так и методы класса для симуляции различных действий. Программа
должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать
методы, взаимодействие объектов и т.д.

"""
from datetime import datetime
from datetime import timedelta


class Person(object):
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name


class Customer(Person):
    def __init__(self, f_name, l_name, money):
        super().__init__(f_name, l_name)
        self.money = money
        self.tickets = []


class Seller(Person):
    def __init__(self, f_name, l_name, works_today):
        super().__init__(f_name, l_name)
        self.works_today = works_today


class Ticket(object):
    def __init__(self, _from, _to, cost, place, _datetime, in_stock=True):
        self._from = _from
        self._to = _to
        self.cost = cost
        self.in_stock = in_stock
        self.place = place
        self.datetime = _datetime


class TicketOffice(object):
    def __init__(self, address, sellers, tickets, revenue=0):
        self.address = address
        self.sellers = sellers
        self.tickets = tickets
        self.revenue = revenue

    @property
    def tickets_in_stock(self):
        in_stock_tickets = set()
        for ticket in self.tickets:
            if ticket.in_stock:
                in_stock_tickets.add(ticket)
        return in_stock_tickets

    @classmethod
    def check_rout(cls, ticket, _from, _to):
        if isinstance(ticket, Ticket):
            if (ticket._from, ticket._to) == (_from, _to):
                return True
        return False

    def sell_ticket(self, seller, ticket, _from, _to, customer):
        if all(
                (
                    ticket in self.tickets_in_stock,
                    self.check_rout(ticket, _from, _to),
                    seller in self.sellers,
                    seller.works_today,
                    customer.money >= ticket.cost,
                )
        ):
            ticket.in_stock = False
            ticket.sale_date = datetime.now()
            self.revenue += ticket.cost
            customer.money -= ticket.cost
            customer.tickets.append(ticket)
            print('Ticket sold')
            return True
        else:
            print('Ticket cannot be sold')
            return False

    def return_ticket(self, seller, ticket, customer):
        if all(
                (
                    hasattr(ticket, 'sale_date'),
                    ticket in customer.tickets,
                    seller in ticket_office.sellers,
                    seller.works_today,
                    datetime.now() < ticket.datetime - timedelta(days=1)
                )
        ):
            ticket.in_stock = True
            self.revenue -= ticket.cost
            customer.money += ticket.cost
            customer.tickets.remove(ticket)
            delattr(ticket, 'sale_date')
            print('Ticket return into ticket-office')
            return True
        else:
            print('Ticket cannot be returned')
            return False


if __name__ == "__main__":
    Vasya_Pupkin = Customer('Vasya', 'Pupkin', 50)
    Ivan_Ivanov = Customer('Ivan', 'Ivanov', 30)
    Nikola_Prusikin = Seller('Nikola', 'Prusikin', works_today=True)
    Linda_Vasilek = Seller('Linda', 'Vasilek', works_today=False)
    ticket_1 = Ticket(
        _from='Paris',
        _to='Warsaw',
        cost=35,
        place=23,
        _datetime=datetime(year=2020, month=5, day=23, hour=11, minute=12)
    )
    ticket_2 = Ticket(
        _from='Prague',
        _to='Dresden',
        cost=23,
        place=15,
        _datetime=datetime(year=2020, month=5, day=25, hour=12, minute=34)
    )
    ticket_3 = Ticket(
        _from='Minsk',
        _to='Berlin',
        cost=78,
        place=11,
        _datetime=datetime(year=2020, month=5, day=26, hour=6, minute=25)
    )
    ticket_office = TicketOffice(
        address='Nezalezhnasti, 15',
        tickets=[ticket_1, ticket_2, ticket_3],
        sellers=[Nikola_Prusikin, Linda_Vasilek]
    )
    # test with correct params
    assert ticket_office.sell_ticket(
        seller=Nikola_Prusikin,
        ticket=ticket_1,
        _from='Paris',
        _to='Warsaw',
        customer=Vasya_Pupkin,
    )
    assert ticket_office.revenue == ticket_1.cost
    assert Vasya_Pupkin.money == 15
    assert not ticket_1.in_stock
    assert hasattr(ticket_1, 'sale_date')
    assert ticket_1 in Vasya_Pupkin.tickets

    # test with incorrect params

    # customer has not enough money
    assert not ticket_office.sell_ticket(
        seller=Nikola_Prusikin,
        ticket=ticket_2,
        _from='Prague',
        _to='Dresden',
        customer=Vasya_Pupkin,
    )
    assert ticket_2.in_stock

    # incorrect directions in ticket and deal
    Vasya_Pupkin.money = 100
    assert not ticket_office.sell_ticket(
        seller=Nikola_Prusikin,
        ticket=ticket_2,
        _from='Minsk',
        _to='Dresden',
        customer=Vasya_Pupkin,
    )
    assert ticket_2.in_stock

    # no ticket available
    assert not ticket_office.sell_ticket(
        seller=Nikola_Prusikin,
        ticket=ticket_1,
        _from='Paris',
        _to='Warsaw',
        customer=Vasya_Pupkin,
    )
    assert len(Vasya_Pupkin.tickets) == 1

    # seller don't work today
    assert Vasya_Pupkin.money == 100
    assert not ticket_office.sell_ticket(
        seller=Linda_Vasilek,
        ticket=ticket_2,
        _from='Prague',
        _to='Dresden',
        customer=Vasya_Pupkin,
    )
    assert ticket_2.in_stock

    # return ticket
    assert not ticket_1.in_stock
    assert ticket_1 in Vasya_Pupkin.tickets
    assert Vasya_Pupkin.money == 100
    assert ticket_office.revenue == ticket_1.cost

    assert ticket_office.return_ticket(
        seller=Nikola_Prusikin,
        ticket=ticket_1,
        customer=Vasya_Pupkin,
    )
    assert ticket_office.revenue == 0
    assert not hasattr(ticket_1, 'sale_date')
    assert not (ticket_1 in Vasya_Pupkin.tickets)
    assert ticket_1.in_stock
    assert Vasya_Pupkin.money == 100 + ticket_1.cost
