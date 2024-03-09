class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types: {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all_pets.append(self)

    def get_all_pets(cls):
        return cls.all_pets


class Owner:
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def pets(self):
        return self.owned_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet class.")
        self.owned_pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.owned_pets, key=lambda x: x.name)
        return sorted_pets
