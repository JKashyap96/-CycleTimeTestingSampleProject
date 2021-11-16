from main import Add
from main import Sub
from main import Mul
from main import Div


def TestAdd():
        #1st Set
        assert Add(2,3) == 5
        assert Sub(2,3) == -1
        assert Mul(2,3) == 6
        assert Div(3,3) == 1
        #2nd Set
        assert Add(3,3) == 6
        assert Sub(6,3) == 3
        assert Mul(2,45) == 90
        assert Div(6,3) == 2
        #3rd Set
        assert Add(5,3) == 8
        assert Sub(90,3) == 87
        assert Mul(2,.5) == 1
        assert Div(6,4) == 1.5
        #4th Set
        assert Add(5,3) == 8
        assert Sub(90,3) == 87
        assert Mul(2,.5) == 1
        assert Div(6,4) == 1.5
        #5th Set
        assert Add(5,3) == 8
        assert Sub(90,3) == 87
        assert Mul(2,.5) == 1
        assert Div(6,4) == 1.5
