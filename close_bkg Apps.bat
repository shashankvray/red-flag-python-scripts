@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"

set /p var="Terminate Teams as well? (Enter/a_z)   : "
echo %var%|findstr "^[A-Za-z]*$" >nulx
if %errorlevel% == 1 (taskkill /F /IM "Teams.exe" /T)


taskkill /F /IM "FortiClient.exe" /T
CALL "C:\Program Files\Fortinet\FortiClient\FortiTray.exe" --shutdown
taskkill /F /IM "Spotify.exe" /T
taskkill /F /IM "ntoskrnl.exe" /T
taskkill /F /IM "OUTLOOK.exe" /T
taskkill /F /IM "PowerToys.exe" /T
taskkill /F /IM "Widgets.exe" /T
taskkill /F /IM "PowerToys.FancyZones.exe" /T
taskkill /F /IM "msedgewebview2.exe" /T
taskkill /F /IM "PowerToys.PowerLauncher.exe" /T
taskkill /F /IM "HxTsr.exe" /T
taskkill /F /IM "FortiSSLVPNdaemon.exe" /T
taskkill /F /IM "FCDBLog.exe" /T
taskkill /F /IM "FortiTray.exe" /T
taskkill /F /IM "SearchIndexer.exe" /T
taskkill /F /IM "ETDCtrl.exe" /T
taskkill /F /IM "ETDTouch.exe" /T
taskkill /F /IM "Taskmgr.exe" /T
taskkill /F /IM "SysInfoCap.exe" /T
taskkill /F /IM "wscript.exe" /T
taskkill /F /IM "vpnui.exe" /T
taskkill /F /IM "cscript.exe" /T
taskkill /F /IM "OfficeClickToRun.exe" /T
taskkill /F /IM "OneDrive.exe" /T
taskkill /F /IM "httpd.exe" /T
taskkill /F /IM "postgres.exe" /T
taskkill /F /IM "pg_ctl.exe" /T
taskkill /F /IM "Cortana.exe" /T
taskkill /F /IM "vpnagent.exe" /T
taskkill /F /IM "Discord.exe" /T
taskkill /F /IM "TouchpointAnalyticsClientService.exe" /T
taskkill /F /IM "KiteService.exe" /T
taskkill /F /IM "Kite.exe" /T
taskkill /F /IM "Kited.exe" /T
taskkill /F /IM "msedge.exe" /T
taskkill /F /IM "TouchpointAnalyticsClientService.exe" /T
taskkill /F /IM "notepad++.exe.exe" /T
taskkill /F /IM "spoolsv.exe" /T
taskkill /F /IM "YourPhoneServer.exe" /T
taskkill /F /IM "YourPhone.exe" /T
taskkill /F /IM "FortiSettings.exe" /T
taskkill /F /IM "HxTsr.exe" /T
taskkill /F /IM "UserOOBEBroker.exe" /T

del "%USERPROFILE%\OneDrive - Profinch Solutions Private Limited\Desktop\nulx" /s /f /q
rmdir "%TEMP%\" /q /s
@taskkill /f /im explorer.exe >nul
@start explorer.exe >nul
del "%TEMP%\*.*" /s /f /q

REM pause