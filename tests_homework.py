import pytest 
from main import vote, solution, check_age

@pytest.mark.parametrize(
        'votes,expected',(
        [[1,1,1,1,2,2,], 1],
        [[2,2,1,4,4,1,1,2,2,], 2],
        [[3,3,3,3,3,11,123,3], 3]
))
def test_vote(votes, expected):
    actual = vote(votes)
    assert actual == expected

@pytest.mark.parametrize(
        'a,b,c,excepted',(
        [1, 8, 15, [-3, -5]],
        [1, -13, 12, [12, 1]],
        [-4, 28, -49, 3.5],
        [1, 1, 1, None]
))
def test_solution(a, b, c, excepted):
    actual = solution(a, b, c)
    assert actual == excepted

@pytest.mark.parametrize(
        'age,excepted',(
        [17, False],
        [18, True],
        [19, True],
))
def test_check_age(age, excepted):
    actual = check_age(age)
    assert actual == excepted

