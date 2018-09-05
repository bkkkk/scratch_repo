from recommendation_enginer import *
import pytest


def test_guess_gender_throws_given_none():
    with pytest.raises(ValueError):
        guess_gender(None)


def test_guess_gender_throws_with_empty_string():
    with pytest.raises(ValueError):
        guess_gender('')


def test_guess_human_gender_does_not_throw_with_valid_string():
    guess_human_gender("blarg")


def test_guess_human_gender_returns_female_with_female_name():
    assert 'female' == guess_human_gender('ana')


def test_guess_human_gender_returns_male_with_male_name():
    assert 'male' == guess_human_gender('john')


def test_guess_gender_returns_florborg_with_florborg_name():
    assert 'florborg' == guess_gender('000111')
