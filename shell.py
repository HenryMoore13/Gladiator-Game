from core import *
from time import sleep


def action():
    player1 = new_gladiator(100, 0, 5, 15)
    player2 = new_gladiator(100, 0, 5, 15)
    sleep(1.5)
    print("  _            ,'|     _ |`,      _            ,'|     _ |")
    print(' (:\          ///     /:) \\\\\    (:\          ///     /:)')
    print('  \:\        )//     /:/   \\\\(    \:\        )//     /:/')
    print(' ==\:(======/:(=====):/=====):\====\:(======/:(=====):/===')
    print('    )\\\\    /:/     //(       \:\    )\\\\    /:/     //')
    print('     \\\\\  (:/     ///         \:)    \\\\\  (:/     ///')
    print("      `.|  \"     |.'           \"      `.|  \"     |.'")

    print('                              .-.')
    print('                             {{#}}')
    print('             {}               8@8')
    print("           .::::.             888")
    print("       @\\\\/W\/\/W\//@         8@8")
    print("        \\\\/^\/\/^\//     _    )8(    _")
    print("         \_O_{}_O_/     (@)__/8@8\__(@)")
    print('    ____________________ `~"-=):(=-"~`')
    print('   |<><><>  |  |  <><><>|     |.|')
    print('   |<>      |  |      <>|     |S|')
    print("   |<>      |  |      <>|     |'|")
    print('   |<>   .--------.   <>|     |.|')
    print('   |     |   ()   |     |     |P|')
    print("   |_____| (O\/O) |_____|     |'|'")
    print('   |     \   /\   /     |     |.|')
    print('   |------\  \/  /------|     |U|')
    print("   |       '.__.'       |     |'|'")
    print('   |        |  |        |     |.|')
    print('   :        |  |        :     |N|')
    print("    \       |  |       /      |'|'")
    print('     \<>    |  |    <>/       |.|')
    print('      \<>   |  |   <>/        |K|')
    print("       `\<> |  | <>/'         |'|'")
    print('         `-.|__|.-`           \ /')
    print('                               ^')

    print('In every battle there comes a time when both sides')
    print('    consider themselves beaten, then he who')
    print('         continues the attack wins.\n')
    print("  _            ,'|     _ |`,      _            ,'|     _ |")
    print(' (:\          ///     /:) \\\\\    (:\          ///     /:)')
    print('  \:\        )//     /:/   \\\\(    \:\        )//     /:/')
    print(' ==\:(======/:(=====):/=====):\====\:(======/:(=====):/===')
    print('    )\\\\    /:/     //(       \:\    )\\\\    /:/     //')
    print('     \\\\\  (:/     ///         \:)    \\\\\  (:/     ///')
    print("      `.|  \"     |.'           \"      `.|  \"     |.'")
    sleep(7)
    print('\n       Lets Get This Fight Started!!!!\n')
    sleep(2)
    while True:
        while True:
            if is_dead(player1):
                print('\n        (Player2 Wins)       ')
                return
            print('                                 /\\')
            print(' ________________________________)(              _')
            print('<________PLAYER1________________(**)@@@@@@@@@@@@(_)')
            print('                                 )(')
            print('                                 \/')
            print('\nGladiator 1:    {} HP ||| {} Rage  '.format(
                player1['health'], player1['rage']))
            print('Gladiator 2:    {} HP ||| {} Rage  '.format(
                player2['health'], player2['rage']))
            print('\n (1) Attack   (2) Heal   (3) Pass   (4) Quit')
            play = input(
                'Gladiator 1... What would you like to do? ').strip().upper()
            if play == '1':
                attack(player1, player2)
                break
            elif play == '2':
                heal(player1)
                break
            elif play == '3':
                wait(player1)
                break
            elif play == '4':
                print('GoodBye')
                break
            else:
                print('Invalid Choice .... Choose (1) (2) (3) (4)')

        while True:
            if is_dead(player2):
                print('\n        (Player1 Wins)      ')
                return
            print('              O')
            print('              {_____________________________________')
            print('@XXXXXXXXXXXXXX_________________PLAYER2____________.>')
            print('              {')
            print('              O')

            print('\nGladiator 1:    {} HP ||| {} Rage  '.format(
                player1['health'], player1['rage']))

            print('Gladiator 2:    {} HP ||| {} Rage  '.format(
                player2['health'], player2['rage']))
            print('\n (1) Attack   (2) Heal   (3) Pass   (4) Quit')
            play = input(
                'Gladiator 2... What would you like to do? ').strip().upper()
            if play == '1':
                attack(player2, player1)
                break
            elif play == '2':
                heal(player2)
                break
            elif play == '3':
                wait(player2)
                break
            elif play == '4':
                print('GoodBye')
                break
            else:
                print('Invalid Choice .... Choose (1) (2) (3) (4)')


def main():
    action()


if __name__ == '__main__':
    main()
