class Country:
    def __init__(self, name: str, country_code: str, location: tuple) -> None:
        self.name = name
        self.country_code = country_code.lower()
        self.location = location

    def to_dict(self):
        return {
            "name": self.name,
            "country_code": self.country_code,
            "location": self.location
        }