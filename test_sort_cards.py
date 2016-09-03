# -*- coding: utf -8 -*-
import pytest
from sort_cards import sort_cards

TEST = [
    ((list('39A5T824Q7J6K')), list('A23456789TJQK')),
    ((list('Q286JK395A47T')), list('A23456789TJQK')),
    ((list('54TQKJ69327A8')), list('A23456789TJQK')),
]


@pytest.mark.parametrize('shuffled, sorted', TEST)
def test_sort_cards(shuffled, sorted):
    '''Test if shuffled cards get sorted as desired.'''
    assert sort_cards(shuffled) == sorted
