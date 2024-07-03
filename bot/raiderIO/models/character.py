class Character:

    def __init__(
        self,
        name: str,
        realm: str,
        guild_name: str,
        faction: str,
        role: str,
        spec_name: str,
        class_name: str,
        achievement_points: int,
        item_level: int,
        score: int,
    ):
        self.name = name
        self.realm = realm
        self.guild_name = guild_name
        self.faction = faction
        self.role = role
        self.spec_name = spec_name
        self.class_name = class_name
        self.achievement_points = achievement_points
        self.item_level = item_level
        self.score = score
