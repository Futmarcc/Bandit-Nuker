@echo off
mode 45,30
set /a num=%random% %%9
color %num%
title      BANDIT IP Pinger     $     Marcc#6666
echo IP PINGER MADE BY Marcc#6666
echo Lets get started!
set /p ip="[-->] Enter IP: "
:top
PING -n 1 %IP% | FIND "TTL=">nul
IF ERRORLEVEL 1 goto offline
IF NOT ERRORLEVEL 1 goto ping
:ping
::set /a num=%random% %%9
::color %num%
title      BANDIT Pinger     $     Marcc#6666     $     Exit - Offline
echo [40;37m [41;37m%IP%[40;30m [40;37mis [42;37mpinging[40;30m
ping localhost -n 2 >nul
goto top
:offline
title      BANDIT Pinger     $     Marcc#6666     $     Exit - Offline
echo [40;37m [41;33m%IP%[40;31m got pinged
ping localhost -n 2 >nul
goto top