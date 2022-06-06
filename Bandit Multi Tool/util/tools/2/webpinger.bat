@echo off
title      BANDIT Website Pinger     $     Marcc#6666
echo Web Pinger made by Marcc#6666
echo Lets get started!
color 2
set /p IPADDRESS="[-->] Enter IP: "
set INTERVAL=3
:PINGINTERVAL
ping google.com
timeout %INTERVAL%
GOTO PINGINTERVAL