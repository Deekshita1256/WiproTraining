import pytest
from src.calculations import Calculations

class TestCalculations:
    calc = Calculations()

    @pytest.fixture(scope="module", autouse=True)
    def setup(self):
        print("Fixture")

    @pytest.mark.parametrize("n1, n2, exval",
                             [(5, 5, 10), (-5, -5, -10), (0, 5, 5)])
    def test_add(self, n1, n2, exval):
        res = self.calc.add(n1, n2)
        assert res == exval, 'Addition Error'

    # def test_add(self):
    #     res = self.calc.add(10, 5)
    #     assert res == 15, 'Addition error'

    @pytest.mark.parametrize("n1, n2, exval",
                             [(5, 5, 0), (-5, -5, 0), (0, 5, -5)])

    def test_sub(self, n1, n2, exval):
        res = self.calc.sub(n1, n2)
        assert res == exval, 'Subtraction Error'

    # def test_sub(self):
    #     res = self.calc.sub(10, 5)
    #     assert res == 5, 'Subtraction Error'

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'Multiplication Error'

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2.0, 'Division Error'

    @pytest.mark.skip(reason = 'NIY')

    def test_ne(self):
        res = self.calc.ne(10, 10)
        assert res == True, 'NE Error'


    @pytest.mark.xfail(reason = 'Except not handled')
    def test_diverr(self):
        #with pytest.raises(ZeroDivisionError):
        res = self.calc.div(10, 0)
        assert res == 0, 'Driverr error'

    # def test_diverr(self):
    #     with pytest.raises(ZeroDivisionError):
    #         self.calc.div(10, 0)


# @pytest.fixture()
# def calc():
#     return Calculations()
#
# def test_add(calc):
#     res = calc.add(10, 5)
#     assert res == 15, 'Addition Error'
#
# def test_sub(calc):
#     res = calc.sub(10, 5)
#     assert res == 5, 'Subtraction Error'
#
# def test_mul(calc):
#     res = calc.mul(10, 5)
#     assert res == 50, 'Multiplication Error'
#
# def test_div(calc):
#     res = calc.div(10, 5)
#     assert res == 2.0, 'Division Error'
#
# def test_ne(calc):
#     res = calc.ne(10, 10)
#     assert res == True, 'NE Error'
#
# def test_diverr(calc):
#     with pytest.raises(ZeroDivisionError):
#         calc.div(10, 0)
