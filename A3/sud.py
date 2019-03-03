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

    pokemon = character.character_information()

    while pokemon["HP"] > 0:
        move_position.move_character(pokemon)


if __name__ == '__main__':
    main()
