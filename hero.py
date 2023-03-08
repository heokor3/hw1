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


hero = Superhero("Адыл", "axe", "резак", 666 , "за войну")

print(hero.names())
print(hero.hpx2())
print(hero.__str__())
print(hero.__len__())

