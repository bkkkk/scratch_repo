from recommendation_enginer import *


def test_api_builder_returns_correct_api_query():
    assert 'https://api.genderize.io/?name=ana' == build_api_call('ana')
