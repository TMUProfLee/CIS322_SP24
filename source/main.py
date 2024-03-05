import sys
import os

from flask import Flask

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "../"))

from CardGames import *
from pyscript import document


def call(event):
    billy = Player("Billy")
    pot = Pot()
    billy.addMoney(50)
    input_text = document.querySelector("#call_amount")
    amount = parsInt(input_text.value)
    output_div = document.querySelector("#output")
    output_div.innerText = Call(billy, amount, pot)

