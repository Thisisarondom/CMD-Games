@echo off
setlocal enabledelayedexpansion
cls
:menu
cls
color 0A
 echo ====================================================
 echo                    CMD GAMES MENU
 echo ====================================================
 echo.
 echo 1. Tetris
 echo 2. Snake
 echo 3. Flappy Bird
 echo 4. Tic Tac Toe (vs Computer)
 echo 5. Exit
 echo.
 set /p choice=Choose a game [1-5]: 

 if "%choice%"=="1" goto play_tetris
 if "%choice%"=="2" goto play_snake
 if "%choice%"=="3" goto play_flappy
 if "%choice%"=="4" goto play_ttt
 if "%choice%"=="5" exit /b 0

 echo Invalid choice.
 timeout /t 1 >nul
 goto menu

:play_tetris
 call :run_python "tetris.py"
 goto menu

:play_snake
 call :run_python "snake.py"
 goto menu

:play_flappy
 call :run_python "flappy_bird.py"
 goto menu

:play_ttt
 call :run_python "tic_tac_toe.py"
 goto menu

:run_python
 set "script=%~1"
 where py >nul 2>nul
 if not errorlevel 1 (
   py -3 "%~dp0%script%"
   exit /b 0
 )
 where python >nul 2>nul
 if not errorlevel 1 (
   python "%~dp0%script%"
   exit /b 0
 )
 echo Python is required to run the games.
 echo Install Python 3 and make sure 'py' or 'python' is on PATH.
 pause
 exit /b 0
