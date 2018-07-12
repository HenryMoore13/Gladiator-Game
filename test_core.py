from core import *


def test_new_gladiator():
    assert new_gladiator(100, 0, 10, 20) == {
        'health': 100,
        'rage': 0,
        'damage_low': 10,
        'damage_high': 20
    }

    assert new_gladiator(50, 10, 15, 25) == {
        'health': 50,
        'rage': 10,
        'damage_low': 15,
        'damage_high': 25
    }


def test_attack_no_rage():
    attacker = new_gladiator(100, 0, 15, 15)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)
    assert defender.get('health') == 85
    assert attacker.get('rage') == 15


def test_attack_with_rage():
    attacker = new_gladiator(100, 100, 20, 40)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)
    assert defender.get('health') >= 20 and defender['health'] <= 60
    assert attacker.get('rage') == 0
