# Домашнє завдання до теми «Алгоритми роботи з великими даними»
## Завдання 1. Перевірка унікальності паролів за допомогою фільтра Блума
Створіть функцію для перевірки унікальності паролів за допомогою фільтра Блума. Ця функція має визначати, чи використовувався пароль раніше, без необхідності зберігати самі паролі.

### Технічні умови
1. Реалізуйте клас `BloomFilter`, який забезпечує додавання елементів до фільтра та перевірку наявності елемента у фільтрі.
2. Реалізуйте функцію `check_password_uniqueness`, яка використовує екземпляр `BloomFilter` та перевіряє список нових паролів на унікальність. Вона має повертати результат перевірки для кожного пароля.
3. Забезпечте коректну обробку всіх типів даних. Паролі слід обробляти просто як рядки, без хешування. Порожні або некоректні значення також мають бути враховані та оброблені належним чином.
4. Функція та клас мають працювати з великими наборами даних, використовуючи мінімум пам’яті.

### Приклад використання
```commandline
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
        print(f"Пароль '{password}' - {status}.")

```
#### Результат
```commandline
Пароль 'password123' — вже використаний.
Пароль 'newpassword' — унікальний.
Пароль 'admin123' — вже використаний.
Пароль 'guest' — унікальний.
```

## Завдання 2. Порівняння продуктивності HyperLogLog із точним підрахунком унікальних елементів
Створіть скрипт для порівняння точного підрахунку унікальних елементів та підрахунку за допомогою HyperLogLog.

### Технічні умови
1. Завантажте набір даних із реального лог-файлу `lms-stage-access.log`, що містить інформацію про IP-адреси.
2. Реалізуйте метод для точного підрахунку унікальних IP-адрес за допомогою структури `set`.
3. Реалізуйте метод для наближеного підрахунку унікальних IP-адрес за допомогою HyperLogLog.
4. Проведіть порівняння методів за часом виконання.

#### Приклад виводу результатів:
```commandline
Результати порівняння:
                       Точний підрахунок   HyperLogLog
Унікальні елементи              100000.0      99652.0
Час виконання (сек.)                0.45          0.1
```
### Порівняння продуктивності HyperLogLog із точним підрахунком унікальних елементів:
```commandline
Результати порівняння:
                        Точний підрахунок   HyperLogLog
Унікальні елементи      28                  28
Час виконання (сек.)    0.001               0.038965
```
#### Точний підрахунок
- Переваги на малих наборах даних:
  - Операції виконуються швидко (все міститься в кеші процесора);
  - Мінімальні накладні витрати на створення структур даних;
  - Відсутність додаткових обчислень (хешування);

- Обмеження:
  - Лінійне зростання використання пам'яті O(n);
  - Зниження продуктивності на дуже великих наборах даних;

#### HyperLogLog
- Переваги на великих наборах даних:
  - Мінімальне використання пам'яті O(1) незалежно від розміру вхідних даних)
  - Час виконання майже не залежить від розміру вхідного набору
  - Ефективна робота з мільйонами та мільярдами унікальних значень
  - Можливість ефективної паралелізації та об'єднання результатів у розподілених системах

- Обмеження:
  - Додаткові витрати на хешування всіх елементів
  - Приблизність результату (похибка 2-3%)
  - Менша ефективність на малих наборах даних


Отже, для малих та середніх наборів даних оптимальним є використання точного підрахунку
Для великих наборів даних, де важлива економія пам'яті та прийнятна невелика похибка, рекомендується HyperLogLog.
Точку перетину продуктивності алгоритмів варто визначати емпірично для конкретної задачі та обладнання.
Обидва алгоритми мають своє місце в обробці даних і вибір між ними залежить від конкретних вимог до точності, використання ресурсів та швидкодії.
