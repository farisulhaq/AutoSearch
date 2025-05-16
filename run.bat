@echo off
title Menjalankan search.py di Virtual Environment...

echo ===================================================
echo [INFO] Mengecek virtual environment...

IF NOT EXIST "venv\Scripts\activate.bat" (
    echo [INFO] Virtual environment belum ada. Membuat virtual environment...
    python -m venv venv
    IF ERRORLEVEL 1 (
        echo [ERROR] Gagal membuat virtual environment.
        goto selesai
    )
) ELSE (
    echo [INFO] Virtual environment sudah ada.
)

echo [INFO] Mengaktifkan virtual environment...
call venv\Scripts\activate.bat

IF ERRORLEVEL 1 (
    echo [ERROR] Gagal mengaktifkan virtual environment.
    goto selesai
)

REM Cek apakah dependencies sudah terinstall
echo [INFO] Mengecek dependencies...
python -c "import pyautogui" 2>NUL
IF %ERRORLEVEL% NEQ 0 (
    echo [INFO] Dependencies belum lengkap. Menginstall dari requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo [INFO] Semua dependencies sudah terinstall.
)

REM Jalankan program
echo ===================================================
echo [INFO] Menjalankan aplikasi Python (search.py)...
python search.py

IF ERRORLEVEL 1 (
    echo [ERROR] Program search.py gagal dijalankan.
)

echo ===================================================
echo [INFO] Program selesai dijalankan.

REM Deactivate venv
deactivate

:selesai
REM Tunggu 5 detik sebelum menutup
echo [INFO] Menutup dalam 5 detik...
timeout /t 5 >nul
