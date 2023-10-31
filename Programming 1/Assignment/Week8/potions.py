"""

01219114 Computer Programming
Week 8, Long Program Assignment: Potion Shop (V1)
(C) 2023 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

class Potion:
    """
    Represents a potion.

    Attributes:
    name -- the name of the potion; cannot be changed later
    ingredient_value -- integer not less than 0
    ingredients -- a set of strings
    effects -- a list of strings
    """

    def __init__(self, name: str = "Potion"):
        """
        Create a new Potion. Its name can be specified.
        If name is not specified, then it is simply called "Potion".
        Do not change the case of potion names.

        >>> Potion('a').name
        'a'
        >>> Potion().name
        'Potion'
        >>> Potion().ingredients
        []
        >>> Potion().ingredient_value
        0
        >>> Potion().effects
        []
        """
        self.name = name
        self.ingredient_value = 0
        self.ingredients = []
        self.effects = []

    def add_ingredient(self, name: str, value: int):
        """
        Add an ingredient. Its name is added to the ingredients list, and
        the value is added to ingredient_value int.
        Do not change the case of ingredient names.

        >>> a = Potion()
        >>> a.ingredient_value
        0
        >>> a.add_ingredient('nirnroot', 10)
        >>> a.ingredient_value
        10
        >>> a.add_ingredient('sweetroll', 2)
        >>> a.ingredient_value
        12
        >>> a.ingredients
        ['nirnroot', 'sweetroll']
        """
        self.ingredients.append(name)
        self.ingredient_value = self.ingredient_value + value

    def ingredient_count(self) -> int:
        """
        Returns the number of ingredients added.

        >>> a = Potion()
        >>> a.ingredient_count()
        0
        >>> a.add_ingredient('troll fat', 15)
        >>> a.ingredient_count()
        1
        >>> a.add_ingredient('troll fat', 15)
        >>> a.ingredient_count()
        2
        >>> a.add_ingredient('nirnroot', 10)
        >>> a.ingredient_count()
        3
        """
        count = len(self.ingredients)
        return count
    
    def add_effect(self, text: str):
        """
        Add an effect. It really doesn't do anything, just being fancy and
        all that. Maintain order of effects, and don't care about same effect
        being added multiple times.

        >>> a = Potion()
        >>> a.effects
        []
        >>> a.add_effect("restore health")
        >>> a.effects
        ['restore health']
        >>> a.add_effect("restore mana")
        >>> a.effects
        ['restore health', 'restore mana']
        """
        self.effects.append(text)

    def clear_effects(self):
        """
        Removes all effects from the potion.
        Doctest is not given for this method.
        """
        self.effects = []

    def sale_price(self) -> int:
        """
        The sale price of the potion is the total ingredient price
        plus 20%, then rounded down.

        >>> a = Potion()
        >>> a.add_ingredient('fire salts', 50)
        >>> a.sale_price()
        60
        >>> a.add_ingredient('nightshade', 8)
        >>> a.sale_price()
        69
        """
        sale_price = int(self.ingredient_value * 0.2)
        total_price = self.ingredient_value + sale_price
        return total_price

    def __eq__(self, other):
        """
        Potions must have identical list of ingredients, effects, and value to be equal.
        The list must be identical. Return false if items are swapped.
        Doctest is not given for this method.

        >>> a = Potion()
        >>> a.add_ingredient('fire salts', 50)
        >>> a.add_ingredient('nightshade', 8)
        >>> a.add_effect('damage health')
        >>> b = Potion()
        >>> b.add_ingredient('fire salts', 50)
        >>> b.add_ingredient('nightshade', 8)
        >>> b.add_effect('damage health')
        >>> a == b
        True
        >>> c = Potion()
        >>> c.add_ingredient('fire salts', 50)
        >>> c.add_ingredient('nightshade', 8)
        >>> b == c
        False
        >>> d = Potion()
        >>> d.add_effect('damage health')
        >>> b == d
        False
        >>> e = Potion()
        >>> e.add_ingredient('nightshade', 8)
        >>> e.add_ingredient('fire salts', 50)
        >>> b == e
        False
        """
        if self.ingredients == other.ingredients:
            if self.effects == other.effects:
                if self.ingredient_value == other.ingredient_value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
# Do not remove this block.
# Doctest will not run otherwise and you won't get score.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
