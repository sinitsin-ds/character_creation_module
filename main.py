from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BREIF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    def __init__(self, name) -> None:
        self.name = name

    def attack(self):
        """Attack the enemy."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        """Block the enemy's attack."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    def special(self):
        """Apply a special skill."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BREIF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BREIF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BREIF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BREIF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    commandos = {
        'attack': Character.attack,
        'defence': Character.defence,
        'special': Character.special
        }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')

        if cmd in commandos:
            print(Character.name, commandos[cmd])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Enter a name and select a character."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, за которого хочешь '
                               'играть: Воитель — warrior, Маг — mage, '
                               'Лекарь — healer: ')
        # Объект выбранного пользователем класса записывается в переменную.
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или '
                               'любую другую кнопку, чтобы выбрать другого '
                               'персонажа ').lower()
    return char_class


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
