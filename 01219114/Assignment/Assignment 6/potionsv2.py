"""

01219114 Computer Programming
Week 10, Long Program Assignment: Potion Shop (V2)
(C) 2023 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
MIT License

"""

class Potion:
    """
    Represents a potion.

    Attributes:
    PRIVATE name -- the name of the potion; cannot be changed later
        has getter, no setter
    PRIVATE ingredients -- a list of strings
        has getter, no setter
    PRIVATE effects -- a list of strings
        has getter, no setter

    To implement sale_price property, you are recommended to also create this:
    PRIVATE ingredient_value -- integer not less than 0
        no getter, no setter

    You must implement @property as required above.
    """

    def __init__(self, name: str='Potion'):
        """
        Create a new Potion. Its name can be specified.
        If name is not specified, then it is simply called "Potion".
        Do not change the case of potion names.

        Must raise TypeError if name is not str.
        Must raise ValueError if name is empty string '' or is a string
        with just spaces '     '.

        >>> Potion('a').name
        'a'
        >>> Potion().name
        'Potion'
        >>> Potion().ingredients
        []
        >>> Potion().effects
        []
        """
        if not isinstance(name, str):
            raise TypeError
        if name.strip() == '':
            raise ValueError
        self.__name = name
        self.__ingredients = []
        self.__effects = []
        self.__ingredient_value = 0

    @property
    def name(self):
        """Get the name of the object."""
        return self.__name

    @property
    def ingredients(self):
        """Get the ingredients of the object."""
        return self.__ingredients

    @property
    def effects(self):
        """Get the effects of the object."""
        return self.__effects

    @property
    def ingredient_value(self):
        """Get the ingredient value of the object."""
        return self.__ingredient_value

    def add_ingredient(self, name: str, value: int):
        """
        Add an ingredient. Its name is added to the ingredients list, and
        the value is added to ingredient_value int.
        Do not change the case of ingredient names.
        
        RAISE TypeError IF NAME IS NOT STR
        RAISE TypeError IF VALUE IS NOT INT
        RAISE ValueError IF NAME IS EMPTY STR OR SPACES ONLY
        RAISE ValueError IF VALUE < 0

        >>> a = Potion()
        >>> a.add_ingredient('nirnroot', 10)
        >>> a.ingredients
        ['nirnroot']
        >>> a.add_ingredient('sweetroll', 2)
        >>> a.ingredients
        ['nirnroot', 'sweetroll']
        >>> a.add_ingredient(10, 10) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError
        >>> a.add_ingredient('sweetroll', -2) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError
        >>> a.add_ingredient('sweetroll', 1.1) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        TypeError
        """
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(value, int):
            raise TypeError
        if name.strip() == '':
            raise ValueError
        if value < 0:
            raise ValueError

        self.__ingredients.append(name.strip())
        self.__ingredient_value = self.__ingredient_value + value

    @property
    def ingredient_count(self) -> int:
        """
        Returns the number of ingredients added.

        >>> a = Potion()
        >>> a.ingredient_count
        0
        >>> a.add_ingredient('troll fat', 15)
        >>> a.ingredient_count
        1
        >>> a.add_ingredient('troll fat', 15)
        >>> a.ingredient_count
        2
        >>> a.add_ingredient('nirnroot', 10)
        >>> a.ingredient_count
        3
        """
        count = len(self.__ingredients)
        return count

    def add_effect(self, text: str):
        """
        Add an effect. It really doesn't do anything, just being fancy and
        all that. Maintain order of effects, and don't care about same effect
        being added multiple times.

        RAISE TypeError IF TEXT IS NOT STR
        RAISE ValueError IF TEXT IS EMPTY STR OR SPACES ONLY

        >>> a = Potion()
        >>> a.effects
        []
        >>> a.add_effect('restore health')
        >>> a.effects
        ['restore health']
        >>> a.add_effect('restore mana')
        >>> a.effects
        ['restore health', 'restore mana']
        """
        if not isinstance(text, str):
            raise TypeError
        if text.strip() == '':
            raise ValueError
        self.__effects.append(text.strip())

    def clear_effects(self):
        """
        Removes all effects from the potion.
        Doctest is not given for this method.
        """
        self.__effects = []

    @property
    def sale_price(self) -> int:
        """
        The sale price of the potion is the total ingredient price
        plus 20%, then rounded down.

        >>> a = Potion()
        >>> a.add_ingredient('fire salts', 50)
        >>> a.sale_price
        60
        >>> a.add_ingredient('nightshade', 8)
        >>> a.sale_price
        69
        """
        sale_price = int(self.__ingredient_value * 0.2)
        total_price = self.__ingredient_value + sale_price
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
        return (
            self.__ingredients == other.__ingredients
            and self.__effects == other.__effects
            and self.__ingredient_value == other.__ingredient_value
        )

    def __add__(self, other):
        """
        You must implement the + operator to mix potions together:
        - Join the lists of ingredients.
        - Join the lists of effects.
        - Add up the values.
        - The new potion is ALWAYS called 'Mixed Potion'.

        >>> a = Potion()
        >>> a.add_ingredient('troll fat', 15)
        >>> a.add_effect('restore health')
        >>> b = Potion()
        >>> b.add_ingredient('nightshade', 8)
        >>> b.add_ingredient('fire salts', 50)
        >>> b.add_effect('restore mana')
        >>> p = a + b
        >>> p.name
        'Mixed Potion'
        >>> p.ingredients
        ['troll fat', 'nightshade', 'fire salts']
        >>> p.effects
        ['restore health', 'restore mana']
        >>> p.sale_price
        87

        """
        mixed_potion = Potion('Mixed Potion')
        mixed_potion.__ingredients = self.__ingredients + other.__ingredients
        mixed_potion.__effects = self.__effects + other.__effects
        mixed_potion.__ingredient_value = self.__ingredient_value + other.__ingredient_value
        return mixed_potion

# Do not remove this block.
# Doctest will not run otherwise and you won't get score.
if __name__ == "__main__":
    import doctest
    doctest.testmod()
