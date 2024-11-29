from src.bun import Bun
from pytest import raises


class TestBun:

    def test_init_bun_with_correct_data(self):
        name = "test"
        price = 42.0
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_init_bun_with_empty_data(self):
        with raises(TypeError):
            Bun()

    def test_get_name(self, bun):
        assert bun.get_name() == bun.name

    def test_get_price(self, bun):
        assert bun.get_price() == bun.price
