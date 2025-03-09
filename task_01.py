import mmh3
from bitarray import bitarray
from typing import List, Dict


class BloomFilter:
    """
    Реалізація фільтра Блума для перевірки унікальності паролів.
    """
    def __init__(self, size: int, num_hashes: int):
        """
        Ініціалізація фільтра Блума.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item: str) -> None:
        """
        Додає елемент у фільтр Блума.
        """
        for i in range(self.num_hashes):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def contains(self, item: str) -> bool:
        """
        Перевіряє, чи є елемент у фільтрі Блума.
        """
        for i in range(self.num_hashes):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False
        return True


def check_password_uniqueness(bloom_filter: BloomFilter, passwords: List[str]) -> Dict[str, str]:
    """
    Перевіряє список паролів на унікальність за допомогою фільтра Блума.
    """
    results = {}
    for password in passwords:
        if not isinstance(password, str) or not password.strip():
            results[password] = "Некоректний пароль"
            continue

        if bloom_filter.contains(password):
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
            bloom_filter.add(password)

    return results


if __name__ == "__main__":
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' — {status}.")