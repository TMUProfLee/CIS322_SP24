from testing_base import *


def test_pot():
    billy = Player("Billy")
    casey = Player("Casey")
    pot = Pot()

    billy.addMoney(50)
    Call(billy, 10, pot)
    print(pot.show_pot())

    casey.addMoney(60)
    Call(casey, 10, pot)
    print(pot.show_pot())

    assert pot.show_pot() == 20


def test_billy():
    billy = Player("Billy")
    casey = Player("Casey")
    pot = Pot()

    billy.addMoney(50)
    Call(billy, 10, pot)
    print(pot.show_pot())

    casey.addMoney(60)
    Call(casey, 10, pot)
    print(pot.show_pot())

    assert billy.money == 40

def test_casey():
    billy = Player("Billy")
    casey = Player("Casey")
    pot = Pot()

    billy.addMoney(50)
    Call(billy, 10, pot)
    print(pot.show_pot())

    casey.addMoney(60)
    Call(casey, 10, pot)
    print(pot.show_pot())

    assert casey.money == 50
  