# CalcNumLock

**Quick calculator toggle + activity tracker + screenshot monitor**

A lightweight system tray app that shows/hides your calculator (or any app) with **NumLock**, tracks active windows, takes smart screenshots, and provides quick productivity tools.

![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

### 🔢 Calculator Hotkey (NumLock)
- Press **NumLock** → show/hide Windows Calculator (or custom app)
- Remembers position, adjustable opacity (10-100%)
- Configure custom exe path + arguments
- **Shift+NumLock** → enable/disable hotkey

### 📊 Activity Tracker
- Tracks active window titles and process names
- Detects idle time (no keyboard/mouse activity)
- Exports to CSV/HTML with time breakdowns
- Auto-archives old data (30+ days → zip)
- Categorize activities: work, social, games, other

### 📸 Smart Screenshots
- **Window change mode**: captures on every window switch
- **Window + timer mode**: window switch + interval (10s / 30s / 1min / 2min / 5min / 10min)
- **Slowdown list**: reduce frequency during video calls/media (Zoom, Teams, VLC, etc.)
- Stores in `_calcnumlock_data/screenshots/YYYY-MM-DD/`

### 🚀 Quick Tools
- **Units menu**: clipboard shortcuts for currencies, measurements (₽, $, €, m², kg, etc.)
- **Quick notes**: write timestamped notes to md/txt/rtf from tray menu
- **Window context**: optional logging of URLs (browsers), Telegram chats, window titles

---

## 🛠️ Installation

### Option 1: Pre-built Executable (Recommended)
1. Download `CalcNumLock.exe` from [Releases](../../releases)
2. Run it — that's it! Creates `_calcnumlock_data/` folder on first launch

### Option 2: Build from Source

**Prerequisites:**
- Python 3.8+ 
- Windows OS

**Steps:**

```bash
# 1. Clone repo
git clone https://github.com/https://github.com/ak9660477713-dotcom/CalcNumLock/CalcNumLock.git
cd CalcNumLock

# 2. Install dependencies
pip install PyQt5 keyboard uiautomation pyinstaller

# 3. Embed icon into .pyw (one-time step)
python patch_embed_icon.py

# 4. Build exe
python build_v2.py --clean

# Result: dist/CalcNumLock.exe
```

---

## 📖 Usage

### First Launch
1. Run `CalcNumLock.exe`
2. Icon appears in system tray (calculator icon)
3. Press **NumLock** → calculator shows up

### Configuration
- **Right-click tray icon** → Settings
- Customize hotkey app, opacity, position, screenshot intervals
- Enable/disable activity tracking, context logging
- Edit units menu (`_calcnumlock_data/units_menu.txt`)

### Activity Reports
- Right-click tray → **Activity Tracker** → **Export Report**
- Choose date range → generates HTML/CSV summary

---

## 📁 Project Structure

```
CalcNumLock/
├── calc_numlock_tray.pyw      # Main application (patched with embedded icon)
├── calculator_icon.ico        # Icon file (for exe build only)
├── patch_embed_icon.py        # Embeds icon into .pyw as base64
├── build_v2.py                # PyInstaller build script
├── README.md                  # This file
└── _calcnumlock_data/         # Created on first run
    ├── config.json            # Settings
    ├── activity_YYYY-MM-DD.csv
    ├── screenshots/
    └── notes.md
```

---

## 🔧 Advanced: Extended Context (Home Mode)

For **URL tracking** (Chrome/Edge/Firefox) and **Telegram chat detection**:

1. Install `uiautomation`: `pip install uiautomation`
2. Create empty file: `_calcnumlock_data/.home`
3. Restart app

Now CSV includes `context` column with URLs and chat names.

---

## 🤝 Contributing

Pull requests welcome! For major changes, open an issue first.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

---

## 🐛 Known Issues

- `keyboard` module requires admin rights on some corporate machines
- Group Policy may block `pip.exe` — use `python -m pip install` instead
- uiautomation warns about missing DLLs if `.home` marker not present (safe to ignore)

---

## 🙏 Credits

- Built with [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Keyboard hooks via [keyboard](https://github.com/boppreh/keyboard)
- Packaged with [PyInstaller](https://pyinstaller.org/)

---

<details>
<summary><b>🇷🇺 Русская версия / Russian version</b></summary>

---

# CalcNumLock

**Быстрый вызов калькулятора + трекер активности + мониторинг скриншотов**

Легковесное приложение в системном трее, которое показывает/скрывает калькулятор (или любое приложение) по **NumLock**, отслеживает активные окна, делает умные скриншоты и предоставляет инструменты для продуктивности.

---

## ✨ Возможности

### 🔢 Горячая клавиша калькулятора (NumLock)
- Нажми **NumLock** → показать/скрыть калькулятор Windows (или кастомное приложение)
- Запоминает позицию, настраиваемая прозрачность (10-100%)
- Настройка пути к exe + аргументы
- **Shift+NumLock** → вкл/выкл горячую клавишу

### 📊 Трекер активности
- Отслеживает заголовки активных окон и имена процессов
- Определяет простой (нет активности клавиатуры/мыши)
- Экспорт в CSV/HTML с разбивкой по времени
- Автоархивация старых данных (30+ дней → zip)
- Категории: работа, соцсети, игры, прочее

### 📸 Умные скриншоты
- **Режим смены окна**: снимок при каждом переключении окна
- **Окно + таймер**: смена окна + интервал (10с / 30с / 1мин / 2мин / 5мин / 10мин)
- **Список замедления**: снижает частоту во время видеозвонков/медиа (Zoom, Teams, VLC и т.д.)
- Хранятся в `_calcnumlock_data/screenshots/YYYY-MM-DD/`

### 🚀 Быстрые инструменты
- **Меню единиц**: быстрая вставка валют, единиц измерения (₽, $, €, м², кг и т.д.)
- **Быстрые заметки**: запись заметок с меткой времени в md/txt/rtf из меню трея
- **Контекст окна**: опциональная запись URL (браузеры), чатов Telegram, заголовков окон

---

## 🛠️ Установка

### Вариант 1: Готовый exe (Рекомендуется)
1. Скачай `CalcNumLock.exe` из [Releases](../../releases)
2. Запусти — готово! При первом запуске создаётся папка `_calcnumlock_data/`

### Вариант 2: Сборка из исходников

**Требования:**
- Python 3.8+
- Windows

**Шаги:**

```bash
# 1. Клонируй репозиторий
git clone https://github.com/https://github.com/ak9660477713-dotcom/CalcNumLock/CalcNumLock.git
cd CalcNumLock

# 2. Установи зависимости
pip install PyQt5 keyboard uiautomation pyinstaller

# 3. Вшей иконку в .pyw (один раз)
python patch_embed_icon.py

# 4. Собери exe
python build_v2.py --clean

# Результат: dist/CalcNumLock.exe
```

---

## 📖 Использование

### Первый запуск
1. Запусти `CalcNumLock.exe`
2. В системном трее появится иконка калькулятора
3. Нажми **NumLock** → появится калькулятор

### Настройка
- **ПКМ по иконке в трее** → Настройки
- Настрой приложение для хоткея, прозрачность, позицию, интервалы скриншотов
- Включи/выключи трекинг активности, логирование контекста
- Отредактируй меню единиц (`_calcnumlock_data/units_menu.txt`)

### Отчёты активности
- ПКМ по трею → **Трекер активности** → **Экспорт отчёта**
- Выбери диапазон дат → генерируется HTML/CSV сводка

---

## 📁 Структура проекта

```
CalcNumLock/
├── calc_numlock_tray.pyw      # Основное приложение (с вшитой иконкой)
├── calculator_icon.ico        # Файл иконки (только для сборки exe)
├── patch_embed_icon.py        # Вшивает иконку в .pyw как base64
├── build_v2.py                # Скрипт сборки PyInstaller
├── README.md                  # Этот файл
└── _calcnumlock_data/         # Создаётся при первом запуске
    ├── config.json            # Настройки
    ├── activity_YYYY-MM-DD.csv
    ├── screenshots/
    └── notes.md
```

---

## 🔧 Дополнительно: Расширенный контекст (домашний режим)

Для **отслеживания URL** (Chrome/Edge/Firefox) и **чатов Telegram**:

1. Установи `uiautomation`: `pip install uiautomation`
2. Создай пустой файл: `_calcnumlock_data/.home`
3. Перезапусти приложение

Теперь в CSV появится колонка `context` с URL и названиями чатов.

---

## 🤝 Вклад в проект

Pull request'ы приветствуются! Для крупных изменений сначала открой issue.

---

## 📄 Лицензия

MIT License — см. файл [LICENSE](LICENSE).

---

## 🐛 Известные проблемы

- Модуль `keyboard` требует прав администратора на некоторых корпоративных машинах
- Групповая политика может блокировать `pip.exe` — используй `python -m pip install`
- uiautomation предупреждает о недостающих DLL, если нет маркера `.home` (можно игнорировать)

---

## 🙏 Благодарности

- Сделано с [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Хуки клавиатуры через [keyboard](https://github.com/boppreh/keyboard)
- Упаковано с [PyInstaller](https://pyinstaller.org/)

</details>
