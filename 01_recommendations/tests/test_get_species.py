from recommendation_enginer import *
import pytest


def test_guess_species_throws_with_invalid_name():
    with pytest.raises(ValueError):
        guess_species('')
        guess_species(None)


def test_guess_species_returns_human_given_human_name():
    assert 'human' == guess_species('ana')


def test_guess_species_returns_florborg_given_florborg_name():
    assert 'florborg' == guess_species('0011')
