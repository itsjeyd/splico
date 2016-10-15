#!/usr/bin/env python

from enum import Enum

# Constants

TOTAL = 0
TOTAL_ANNA = 0
TOTAL_TIM = 0

DEBT_ANNA = 0
DEBT_TIM = 0


# Classes

class Person(Enum):
    ANNA = 'Anna'
    TIM = 'Tim'


# Functions

def read_cost(person):
    global TOTAL, TOTAL_ANNA, TOTAL_TIM
    cost = input('Enter cost for {person} (blank to finish): '.format(person=person.name))
    if not cost:
        return
    cost = float(cost)
    TOTAL += cost
    if person == Person.ANNA:
        TOTAL_ANNA += cost
    elif person == Person.TIM:
        TOTAL_TIM += cost
    read_cost(person)


def print_totals():
    print('======================================')
    print('TOTAL: EUR {total:.2f} (EUR {half:.2f} per person)'.format(
        total=TOTAL,
        half=(TOTAL/2),
    ))
    print('{person} paid: EUR {total:.2f}'.format(
        person=Person.ANNA.name, total=TOTAL_ANNA
    ))
    print('{person} paid: EUR {total:.2f}'.format(
        person=Person.TIM.name, total=TOTAL_TIM
    ))
    print('======================================')


def calculate_debt():
    global DEBT_ANNA, DEBT_TIM
    DEBT_ANNA = (TOTAL / 2) - TOTAL_ANNA
    DEBT_TIM = (TOTAL / 2) - TOTAL_TIM


def print_debt():
    def format_debt(person, debt):
        if debt < 0:
            return '{person} has no debt. {pronoun} is up by EUR {debt:.2f}.'.format(
                person=person.name,
                pronoun='She' if person == Person.ANNA else 'He',
                debt=abs(debt),
            )
        elif debt == 0:
            return '{person} has no debt.'.format(person=person.name)
        if person == Person.ANNA:
            creditor = Person.TIM
        elif person == Person.TIM:
            creditor = Person.ANNA
        return '{person} ows {creditor} EUR {debt:.2f}.'.format(
            person=person.name,
            creditor=creditor.name,
            debt=debt
        )
    print(format_debt(Person.ANNA, DEBT_ANNA))
    print(format_debt(Person.TIM, DEBT_TIM))


def splico():
    read_cost(Person.ANNA)
    read_cost(Person.TIM)
    print_totals()
    calculate_debt()
    print_debt()

if __name__ == '__main__':
    splico()
