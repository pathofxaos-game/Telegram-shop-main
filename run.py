import asyncio
import warnings
import sys
import os

# Подавляем RuntimeWarning
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Добавляем путь
sys.path.append(os.path.dirname(__file__))

# Импортируем и запускаем
from bot.main import start_bot

if __name__ == "__main__":
    print("🚀 Запуск бота...")
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("🛑 Бот остановлен")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
