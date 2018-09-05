from recommendation_enginer import *
import pytest


def test_get_recommednation_throws_with_empty_gender():
    with pytest.raises(KeyError):
        get_recommendation(None)

    with pytest.raises(KeyError):
        get_recommendation('')


def test_get_recommendation_throws_with_invalid_gender():
    with pytest.raises(KeyError):
        get_recommendation('orc')


def test_get_recommendation_with_male_name():
    assert get_recommendation('male') in ['Condoms', 'Male-oriented scented shaving foam', 'Die Hard 4', 'Larger than average shoe']


def test_get_recommendation_with_florborg_name():
    assert get_recommendation('florborg') in ['Oil', 'CPUs', 'Silver suits', 'Warp Cores']
