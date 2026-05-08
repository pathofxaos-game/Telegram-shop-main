import asyncio
import warnings
import sys
import os
import logging

# Полностью отключаем RuntimeWarning
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore", RuntimeWarning)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# Добавляем путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 50)
print("🚀 ЗАПУСК БОТА TELEGRAM SHOP")
print("=" * 50)

try:
    from bot.main import start_bot
    print("✅ Модуль bot.main загружен")
    print("📡 Запуск polling...")
    asyncio.run(start_bot())
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"❌ Критическая ошибка: {e}")
    import traceback
    traceback.print_exc()
