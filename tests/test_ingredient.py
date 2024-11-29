from src.ingredient import Ingredient


class TestIngredient:

    def test_init(self):
        type = "test type"
        name = "test ingredient"
        price = 42.0
        ingredient = Ingredient(type, name, price)
        assert ingredient.type == type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient.type

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient.name

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient.price
