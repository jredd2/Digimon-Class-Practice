class Digimon:
    def __init__(self, name: str, max_armor: int, max_hit: int):
        self.name = name
        self.armor = max_armor
        self.hit_points = max_hit
        self._is_charging = False

    def attack(self):
        print(f"{self.name} attacks")
    def defend(self):
        print(f"{self.name} defends itself")
    def _change_attack(self):
        print(f"{self.name} is changing attack type")

class ElectricDigimon(Digimon):
    def wild_charge(self):
        print(f"{self.name} wild charges")
class WaterDigimon(Digimon):

    def __init__(self, name: str, max_armor: int, max_hit: int, speed: int):
        Digimon.__init__(self, name, max_armor,max_hit)
        self.speed = speed
    def aqua_tail(self):
        print(f"Aqua Tail Splash!!!")
class FlyingDigimon(Digimon):
    def dive_bomb(self):
        print(f"Dive Bomb attack")

metalgraymon = Digimon("MetalGraymon", 100, 1000)
gururumon = WaterDigimon("Gururumon", 99, 99, 100)
jaymon = ElectricDigimon("Jaymon", 190, 2000)
graymon = FlyingDigimon("graymon", 2000, 290)

digimon = (metalgraymon, gururumon, jaymon, graymon)

for digimon in digimon:
    digimon.attack()

MetalGraymon = Digimon("Snorlax", 75, 900)
MetalGraymon.attack()
