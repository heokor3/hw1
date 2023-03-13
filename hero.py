class Superhero:
    people = "people"

    def __init__(self, name, nikname, superpower, health_points, catchphrase):
        self.name = name
        self.nikname = nikname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return self.name

    def hpx2(self):
        return self.health_points * 2

    def __str__(self):
        return f"его имя {self.nikname} его ульта {self.superpower} его здоровье {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = Superhero("Адыл", "axe", "резак", 666, "за войну")


class Hero(Superhero):
    type = "agi"

    def __init__(self, name, nikname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nikname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        return f' Здоровье героя {self.health_points ** 2}'

    def fly_true(self):
        print(f' fly in the True_phrase')

class SecondHero(Superhero):
    type = 'int'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


riki = Hero('Riki', 'Talin', 'invisible', 540, 'Моя речь мягка, но клинок остёр.',damage=61)
invoker = SecondHero('Invoker', 'elf', 'elements', 560, 'Карл!',damage=47)
riki.hp()
riki.fly_true()
invoker.hp()
invoker.fly_sky()
class Villain(Hero):
    Superhero.people = "monster"
    def __init__(self,name,nikname,superpower,health_points,cathphrase):
        super().__init__(self,name,nikname,superpower,health_points,cathphrase)

    def gen_x(self):
        pass
    def crit(self, hero):
        return hero.damage ** 2

razor = Villain('razor', 'the keeper', 'lightnings', 1200, 'Молнии ')
print(Villain.crit(razor, riki))
print(Villain.crit(razor, invoker))

