import sys
import os
import warnings
import asyncio

# 1. Отключаем назойливое предупреждение runpy
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", message=".*found in sys.modules.*")

# 2. Добавляем корень проекта в путь импортов
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# 3. Включаем мгновенный вывод логов (без буферизации)
os.environ["PYTHONUNBUFFERED"] = "1"

print("="*40, flush=True)
print("🚀 ИНИЦИАЛИЗАЦИЯ БОТА", flush=True)
print("="*40, flush=True)

try:
    from bot.main import start_bot
    print("✅ Модуль загружен. Запуск...", flush=True)
    asyncio.run(start_bot())
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
except Exception as e:
    print(f"❌ Критическая ошибка: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
