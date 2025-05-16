import pytest
from owner_pet import Pet, Owner

def test_owner_has_pets():
    """Test Owner class returns all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog")
    pet2 = Pet("Clifford", "dog")
    
   
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    assert owner.pets == [pet1, pet2]

    Pet.all = []

def test_owner_adds_pets():
    """Test add_pet() validates and adds a pet"""
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)

    assert pet.owner == owner
    assert owner.pets == [pet]

    Pet.all = []

def test_get_sorted_pets():
    """Test get_sorted_pets sorts pets by name"""
    owner = Owner("John")
    pet1 = Pet("Fido", "dog")
    pet2 = Pet("Clifford", "dog")
    pet3 = Pet("Whiskers", "cat")
    pet4 = Pet("Jerry", "reptile")

    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)
    owner.add_pet(pet4)

    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]
