from starlette.testclient import TestClient

from climbing_grade_converter.main import app
from climbing_grade_converter.db.database import find_indicies_of_key


client = TestClient(app)


def test_find_index_of_key():
    search_list = ["a", "b", "c"]
    search_key = "a"
    expected_index = [0]
    index = find_indicies_of_key(search_list, search_key)
    assert expected_index == index


def test_find_indicies_of_key():
    search_list = ["a", "a", "b", "b", "c"]
    search_key = "a"
    expected_index = [0, 1]
    index = find_indicies_of_key(search_list, search_key)
    assert expected_index == index


def test_find_no_index_no_key():
    search_list = ["a", "a", "b", "b", "c"]
    search_key = "d"
    expected_index = []
    index = find_indicies_of_key(search_list, search_key)
    assert expected_index == index
