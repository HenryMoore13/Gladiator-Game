from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    return {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


def attack(attacker, defender):
    damage = randint(attacker['damage_low'], attacker['damage_high'])

    if attacker['rage'] > randint(35, 74):
        defender['health'] = defender['health'] - (3 * damage)
        attacker['rage'] = int(attacker['rage'] / 2)
        print('\nPower Punch!!\n')
    else:
        defender['health'] = defender['health'] - damage
        attacker['rage'] = min(attacker['rage'] + 10, 100)


def wait(gladiator):
    gladiator['rage'] = min(gladiator['rage'] + 20, 100)


def heal(gladiator):
    if gladiator['rage'] >= 10:
        health = gladiator['health'] + (gladiator['rage'] // 2)
        gladiator['health'] = min(100, health)
        gladiator['rage'] = 0

    # Spends 10 rage to heal 5 health

    # Cannot heal above max health of 100

    return None


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    return False
