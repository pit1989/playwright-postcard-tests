import requests

print("=" * 50)
print("ТЕСТИРУЕМ API БЕЗ Pytest")
print("=" * 50)

# Тест 1
print("\n📡 Тест 1: Подключаемся к httpbin.org...")
response = requests.get('https://httpbin.org/get')
print(f"   Статус: {response.status_code}")
print(f"   Успешно!" if response.status_code == 200 else f"   Ошибка!")

# Тест 2
print("\n🎯 Тест 2: Проверяем параметры...")
response = requests.get(
    'https://httpbin.org/get',
    params={'trainer': 'Ash', 'pokemon': 'Pikachu'}
)
data = response.json()
print(f"   Параметры в ответе: {data['args']}")

print("\n" + "=" * 50)
print("✅ ВСЁ РАБОТАЕТ!")
print("=" * 50)