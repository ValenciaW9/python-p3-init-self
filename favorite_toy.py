class Dog:
    def __init__(self, name, favoirte_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy

        fido = Dog("Fido")
        fido.favoritye_toy
        # Any

        snoopy = Dog("Snoopy", "Tennis Ball")
        snoopy.favorite_toy
        # Tennis Ball

        old_yelloer = Dog()
        # TypedError: __init__() missing 1 required positional  argument: 'name"
