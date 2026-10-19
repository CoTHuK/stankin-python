"""Проверка IPv4-адресов."""

import re


# Каждый октет должен быть числом от 0 до 255.
_OCTET = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
_IPV4_ = re.compile(rf"{_OCTET}(?:\.{_OCTET}){{3}}")


def is_valid_ip(address: str) -> bool:
    # Проверяет, является ли строка корректным IPv4-адресом.
    if not isinstance(address, str):
        return False
    return _IPV4_.fullmatch(address) is not None
