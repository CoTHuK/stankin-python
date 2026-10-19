import pytest

from email_validator import is_valid_ip


def test_all_valid_fixture_ips(valid_ips):
    for address in valid_ips:
        assert is_valid_ip(address) is True, f"должен быть корректным IPv4: {address!r}"


def test_all_invalid_fixture_ips(invalid_ips):
    for address in invalid_ips:
        assert is_valid_ip(address) is False, f"должен быть некорректным IPv4: {address!r}"


@pytest.mark.parametrize("value", [None, 123, ["192.168.1.1"]])
def test_non_string_values_are_invalid(value):
    assert is_valid_ip(value) is False
