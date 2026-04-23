#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build.py — сборка calc_numlock_tray.pyw в exe через PyInstaller.

ПРЕДВАРИТЕЛЬНОЕ УСЛОВИЕ:
    Запусти patch_embed_icon.py ОДИН РАЗ перед первой сборкой.
    После патча .pyw содержит вшитую иконку в base64.

Использование:
    python build.py              # обычная сборка onefile
    python build.py --onedir     # сборка в папку (запускается быстрее)
    python build.py --clean      # очистить build/dist/spec перед сборкой
    python build.py --install    # перед сборкой поставить зависимости

Результат:
    dist/CalcNumLock.exe — единственный файл, полностью автономен.
    При первом запуске создаст рядом папку _calcnumlock_data/.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Параметры сборки
# ---------------------------------------------------------------------------
HERE        = Path(__file__).resolve().parent
SRC         = HERE / "calc_numlock_tray.pyw"
ICON        = HERE / "calculator_icon.ico"
APP_NAME    = "CalcNumLock"

# Зависимости рантайма. uiautomation — опциональный (только для "домашнего"
# режима с .home маркером), но вшиваем его в exe, чтобы маркер работал
# без переустановки.
RUNTIME_DEPS = [
    "pyinstaller",
    "PyQt5",
    "keyboard",
    "uiautomation",
]

# Скрытые импорты — то, что PyInstaller может не найти автоанализом.
HIDDEN_IMPORTS = [
    "uiautomation",         # грузится через import внутри if IS_HOME
    "keyboard",
    "PyQt5.sip",
]

# Модули, которые точно не нужны в exe — режем, чтобы уменьшить размер.
EXCLUDES = [
    "tkinter",
    "unittest",
    "pydoc",
    "test",
    "distutils",
    "lib2to3",
    "PyQt5.QtWebEngineCore",
    "PyQt5.QtWebEngineWidgets",
    "PyQt5.QtWebEngine",
    "PyQt5.QtQml",
    "PyQt5.QtQuick",
    "PyQt5.QtMultimedia",
    "PyQt5.QtNetwork",
    "PyQt5.QtSql",
    "PyQt5.QtTest",
    "PyQt5.QtXml",
]


def run(cmd: list[str]) -> None:
    print(">>>", " ".join(f'"{x}"' if " " in x else x for x in cmd), flush=True)
    res = subprocess.run(cmd)
    if res.returncode != 0:
        sys.exit(f"\n!! Команда упала с кодом {res.returncode}")


def ensure_deps() -> None:
    print("Устанавливаю зависимости…")
    run([sys.executable, "-m", "pip", "install", "--upgrade", *RUNTIME_DEPS])


def clean() -> None:
    for name in ("build", "dist"):
        p = HERE / name
        if p.exists():
            print(f"Удаляю {p}")
            shutil.rmtree(p, ignore_errors=True)
    for spec in HERE.glob("*.spec"):
        print(f"Удаляю {spec}")
        spec.unlink(missing_ok=True)


def build(onefile: bool) -> None:
    if not SRC.exists():
        sys.exit(f"Не найден исходник: {SRC}")

    # Проверяем, что .pyw пропатчен (содержит ICON_B64)
    src_text = SRC.read_text(encoding="utf-8")
    if "ICON_B64 = " not in src_text:
        print("\n" + "!" * 60)
        print("ВНИМАНИЕ: в .pyw не найдена ICON_B64!")
        print("Похоже, ты ещё не применил patch_embed_icon.py.")
        print("\nЗапусти сначала:")
        print("    python patch_embed_icon.py")
        print("\nПосле этого повтори сборку:")
        print("    python build.py")
        print("!" * 60)
        sys.exit(1)

    args: list[str] = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm",
        "--clean",
        "--windowed",                 # без консольного окна (как .pyw)
        f"--name={APP_NAME}",
        "--onefile" if onefile else "--onedir",
    ]

    # Иконка для ресурсов exe (иконка в проводнике, alt-tab).
    # Сам .pyw уже содержит вшитую иконку в base64, поэтому
    # внешний .ico нужен ТОЛЬКО для --icon (ресурсы бинарника).
    if ICON.exists():
        args += [f"--icon={ICON}"]
    else:
        print(f"  (!) {ICON} не найден — exe будет с дефолтной иконкой.")

    for mod in HIDDEN_IMPORTS:
        args += [f"--hidden-import={mod}"]
    for mod in EXCLUDES:
        args += [f"--exclude-module={mod}"]

    args.append(str(SRC))

    run(args)

    dist_dir = HERE / "dist"
    print("\n" + "=" * 60)
    print("✓ СБОРКА ЗАВЕРШЕНА")
    print("=" * 60)
    print(f"Результат: {dist_dir / (APP_NAME + '.exe' if onefile else APP_NAME)}")
    print("\nЕдинственный файл, полностью автономен.")
    print("При первом запуске создаст рядом _calcnumlock_data/")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--onedir", action="store_true",
                    help="Собрать в папку (быстрее стартует), иначе — onefile.")
    ap.add_argument("--clean", action="store_true",
                    help="Перед сборкой удалить build/dist/*.spec.")
    ap.add_argument("--install", action="store_true",
                    help="Перед сборкой поставить/обновить зависимости.")
    args = ap.parse_args()

    if args.install:
        ensure_deps()
    if args.clean:
        clean()

    build(onefile=not args.onedir)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nПрервано.")
