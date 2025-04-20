@echo off
title Menjalankan search.py di Virtual Environment...

echo ===================================================
echo [INFO] Mengaktifkan virtual environment...
call venv\Scripts\activate.bat

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
echo ===================================================
echo [INFO] Program selesai dijalankan.

REM Deactivate venv
deactivate

REM Tunggu 5 detik sebelum menutup
echo [INFO] Menutup dalam 5 detik...
timeout /t 5 >nul
