@echo off
echo [INFO] Menunggu device ADB terhubung...

:loop
:: Cek apakah ada device terhubung
adb devices | findstr /R "device$" >nul
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Device terdeteksi.
    goto mulai
)

:: Jika belum ada device, tunggu 2 detik dan cek lagi
echo [INFO] Tidak ada device terdeteksi. Menunggu 2 detik...
timeout /t 2 >nul
goto loop

:mulai
echo [INFO] Mengaktifkan virtual environment...
call venv\Scripts\activate.bat

echo [INFO] Mengecek dependencies...
python -c "import pyautogui" 2>NUL
IF %ERRORLEVEL% NEQ 0 (
    echo [INFO] Dependencies belum lengkap. Menginstall dari requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo [INFO] Semua dependencies sudah terinstall.
)

echo ===================================================
echo [INFO] Menjalankan aplikasi Python (chrome.py)...
python bing.py
echo ===================================================
echo [INFO] Program (chrome.py) selesai dijalankan.

echo ===================================================
echo [INFO] Menjalankan aplikasi Python (bing.py)...
python chrome.py
echo ===================================================
echo [INFO] Program (bing.py) selesai dijalankan.

REM Deactivate virtual environment
call venv\Scripts\deactivate.bat

echo [INFO] Menutup dalam 5 detik...
timeout /t 5 >nul
