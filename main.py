from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import datetime
import random

from datetime import date
from datetime import timedelta


class LibraryItem(object):
    '''
        Attributes
        ----------
        item_number: unique number of the item
        status: available or borrowed
        borrowing_stats: statistics about the item
    '''

    def __init__(self, item_number):
        self.item_number = item_number
        self.status = 'available'
        self.borrowing_stats = dict()

    def borrow_item(self, personal_number):
        if self.status == 'available':
            self.borrowing_stats[personal_number] = {'Borrowed on': date.today(),
                                                     'Return by': date.today() + timedelta(days=30),
                                                     'Returned on': '-'}
            self.status = 'borrowed'
        else:
            print('Item is already borrowed.')

    def return_item(self, personal_number):
        pass

    def get_info(self):
        print(f'Item type: Library item\
        \nItem number: {self.item_number}\n')

        print(f'The item is currently {self.status}.\n')

        for k, v in self.borrowing_stats.items():
            print(f'Item {k} was borrowed by {v["Borrowed on"]} and should be returned by {v["Return by"]}.')
            print(f'Item {self.item_number} was returned on {v["Returned on"]}.')

            for k1,v1 in v.items():
                print(f'{k1}: {v1}')

            print('\n')


class Book(LibraryItem):
    '''Books in the library'''

    def __init__(self, item_number, title, author, publisher):
        super().__init__(item_number)
        self.title = title
        self.author = author
        self.publisher = publisher

    def get_info(self):
        pass


class CD(LibraryItem):
    '''CDs in the library'''

    def __init__(self, item_number, title):
        super().__init__(item_number)
        self.title = title

    def get_info(self):
        pass


class Member(object):
    pass

item1 = LibraryItem(123)
item2 = LibraryItem(124)
book = Book(125, 'Matilda', 'Roald Dahl', 'Jonathan Cape')
cd = CD(126, 'Matilda')
mem = Member()


item1.borrow_item('98-1201')