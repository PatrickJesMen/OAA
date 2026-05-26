
class Character:
    def __init__(self, name: str, attack_damage: float, health: float, defense: float, agility: float, critical_chance: int, critical_attack_damage: float):
        self._name = name
        self._attack_damage = attack_damage
        self._max_hp = health
        self._health = health
        self._defense = defense
        self._agility = agility
        self._critical_chance = critical_chance
        self._critical_attack_damage = critical_attack_damage

    def get_health(self):
        return self._health

    def get_attack_damage(self):
        return self._attack_damage