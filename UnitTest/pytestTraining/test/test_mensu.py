from src.calculations import Calculations


class TestMensu:
    calc = Calculations()

    def test_area_of_square(self):
        res = self.calc.area_of_square(10)
        assert res == 100, 'Area is Wrong'

    def test_area_of_rect(self):
        res = self.calc.area_of_rect(10, 5)
        assert res == 50, 'Area is wrong'