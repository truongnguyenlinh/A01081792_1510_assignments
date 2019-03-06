import character
import move_position


def main():
    print("______________________________________________________________________")
    print("[]    ,-`  ,-`’```’-,:`’-,       \                      ,--,:`,     []")
    print("[]   ,/  /`           `’-,:`’-,   \,-     ,,,         ./¯¯) `)\     []")
    print("[]   |  |                  `-,:`’- /    ,/¯) .\       |¯¯. ,/`’/’   []")
    print("[]   \  |                     `’-,’,    ( ¯’__|        ¯¯¯   ,-`    []")
    print("[]   `\  \                        ‘’`-,   ¯¯                ,’-`    []")
    print("[]     \   \                       '-_/’-‘--,- ---,, __,,-`         []")
    print("======================================================================")

    character.character_information()

    while character.get_pokemon()["HP"] > 0:
        move_position.move_character()


if __name__ == '__main__':
    main()
