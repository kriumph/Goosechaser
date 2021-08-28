# You will need to import the Creature class.
from creature import Creature
from item import Item

def test_creatures_1():
    Pikachu = Creature('Pikachu',10)
    hat = Item('hat', "Ash's hat", "A new hat received from Ash's mom.", 2, 'Pallet Town')
    Pikachu.take(hat)
    expect = 12
    actual = Pikachu.get_terror_rating()
    assert expect == actual, 'Test 1 failed.'
    
def test_creatures_2():
    Charmander = Creature('Charmander', 10)
    hat = Item('hat', "Ash's hat", "A new hat received from Ash's mom.", 2, 'Pallet Town')
    Charmander.take(hat)
    Charmander.drop(hat)
    expect = 10
    actual = Charmander.get_terror_rating()
    assert expect == actual, 'Test 2 failed.'
    
    
def test_creatures_3():
    Bulbasaur = Creature('Bulbasaur', 10)
    expect = 'Bulbasaur'
    actual = Bulbasaur.name
    assert expect == actual, 'Test 3 failed.'
    
def test_creatures_4():
    Squirtle = Creature('Squirtle', 10)
    expect = 10
    actual = Squirtle.terror_rating
    assert expect == actual, 'Test 4 failed.'
    
def test_creatures_5():
    Togepi = Creature('Togepi', 5)
    hat = Item('hat', "Ash's hat", "A new hat received from Ash's mom.", 2, 'Pallet Town')
    bike = Item('bike', "Misty's bike", "A broken bike of Misty is destroyed by Ash's Pikachu.", 10, 'Cerulean City')
    Togepi.take(bike)
    Togepi.take(hat)
    Togepi.drop(bike)
    Togepi.drop(hat)
    expect = 5
    actual = Togepi.get_terror_rating()
    assert expect == actual, 'Test 5 failed.'
    
test_creatures_1()    
test_creatures_2()    
test_creatures_3()    
test_creatures_4()    
test_creatures_5()
