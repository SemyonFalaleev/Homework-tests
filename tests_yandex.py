from main import YandexDiskApi
import pytest

@pytest.mark.parametrize(
    'token, path, excepted',(
        ["token", "Test1", 201],
        ["token", "Test2", 201],
        ["token", "Test1", 409],
        ["wrong_token", "Test4", 201],
        ["token", "Test2", 201]
    ))
def test_yadisk_create_folder(token, path, excepted):
    ya_disk_api = YandexDiskApi(token)
    actual = ya_disk_api.create_folder(path)
    assert actual == excepted

