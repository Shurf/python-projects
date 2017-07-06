__author__ = 'schrecknetuser'
import typing

class Profile:
    def __init__(self, min_range:int, max_range:int, strength: int, ap:int, shots:float, damage:float):
        self.strength = strength
        self.min_range = min_range
        self.max_range = max_range
        self.ap = ap
        self.shots = shots
        self.damage = damage


class Weapon:

    def is_autohit(self):
        return False

    def __init__(self, name:str, point_cost:int, profiles:typing.List[Profile]):
        self.name = name
        self.point_cost_value = point_cost
        self.profiles = profiles

    def profile(self, range):
        profile = next((x for x in self.profiles if x.min_range < range and x.max_range >= range), None)
        return profile

    def strength(self, range_value:int):
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.strength

    def ap(self, range_value:int) -> int:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.ap

    def shots(self, range_value:int) -> float:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.shots

    def damage(self, range_value:int) -> float:
        profile = self.profile(range_value)
        if profile is None:
            return 0
        return profile.damage

    def point_cost(self):
        return self.point_cost_value

    def name(self):
        return self.name





