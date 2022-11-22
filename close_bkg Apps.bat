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


set /p var="Terminate Teams as well? ([Enter]/a_z)   : "
echo %var%|findstr "^[A-Za-z]*$" > "%TEMP%\nulx"3
Rem --------------------------------------------------------------------------------

if %errorlevel% == 1 (
Rem CLOSE ALL [ off work ]
taskkill /F /IM "Teams.exe" /T
echo "MS TEAMS HAS BEEN ASSASSINATED.... Muahahaha...."
echo:
echo:
taskkill /F /IM "wscript.exe" /T) else (
Rem OPEN TEAMS [ in work ]
CALL "C:\Users\Shashank V Ray\AppData\Local\Microsoft\Teams\Update.exe" --processStart "Teams.exe"
)

taskkill /F /IM "FortiClient.exe" /T
CALL "%USERPROFILE%\OneDrive - Profinch Solutions Private Limited\Java Team - Rahul Agarwal\FORTICLIENT INSTALLATION FOLDER\FortiClient\FortiTray.exe" --shutdown
CALL "C:\Program Files\Fortinet\FortiClient\FortiTray.exe" --shutdown
REM taskkill /F /IM "PowerToys.exe" /T
REM taskkill /F /IM "PowerToys.PowerLauncher.exe" /T
REM taskkill /F /IM "msedge.exe" /T
REM taskkill /F /IM "msedgewebview2.exe" /T
"C:\Users\Shashank V Ray\OneDrive - Profinch Solutions Private Limited\TMB Support\OpenVPN\bin\openvpn-gui.exe" --command disconnect openvpn-shashank.ray-inline.ovpn

taskkill /F /IM "OneDrive.exe" /T
taskkill /F /IM "SSPService.exe" /T
taskkill /F /IM "SophosFileScanner.exe" /T
taskkill /F /IM "TeamViewer_Service.exe" /T
taskkill /F /IM "Appgate SDP Update Service.exe" /T
taskkill /F /IM "TSVNCache.exe" /T
taskkill /F /IM "Taskmgr.exe" /T
taskkill /F /IM "XtuService.exe" /T
taskkill /F /IM "Zoom.exe" /T
taskkill /F /IM "CxAudioSvc.exe" /T
taskkill /F /IM "FCDBLog.exe" /T
taskkill /F /IM "FortiSettings.exe" /T
taskkill /F /IM "FortiSSLVPNdaemon.exe" /T
taskkill /F /IM "TeamViewer.exe" /T
taskkill /F /IM "zWebview2Agent.exe" /T
taskkill /F /IM "plsqldev.exe" /T
taskkill /F /IM "sqldeveloper64W.exe" /T
taskkill /F /IM "WinSCP.exe" /T
taskkill /F /IM "TSVNCache.exe" /T
taskkill /F /IM "ntoskrnl.exe" /T
taskkill /F /IM "OUTLOOK.exe" /T
taskkill /F /IM "MRT.exe" /T
taskkill /F /IM "Windows-KB890830-x64-V5.99.exe" /T
taskkill /F /IM "Widgets.exe" /T
taskkill /F /IM "HxTsr.exe" /T
taskkill /F /IM "FCDBLog.exe" /T
taskkill /F /IM "SearchIndexer.exe" /T
taskkill /F /IM "ETDCtrl.exe" /T
taskkill /F /IM "ETDTouch.exe" /T
taskkill /F /IM "Taskmgr.exe" /T
taskkill /F /IM "SysInfoCap.exe" /T
taskkill /F /IM "vpnui.exe" /T
taskkill /F /IM "cscript.exe" /T
taskkill /F /IM "OfficeClickToRun.exe" /T
taskkill /F /IM "httpd.exe" /T
taskkill /F /IM "postgres.exe" /T
taskkill /F /IM "pg_ctl.exe" /T
taskkill /F /IM "Cortana.exe" /T
taskkill /F /IM "vpnagent.exe" /T
taskkill /F /IM "Discord.exe" /T
taskkill /F /IM "KiteService.exe" /T
taskkill /F /IM "Kite.exe" /T
taskkill /F /IM "Kited.exe" /T
taskkill /F /IM "TouchpointAnalyticsClientService.exe" /T
taskkill /F /IM "spoolsv.exe" /T
taskkill /F /IM "FortiSettings.exe" /T
taskkill /F /IM "HxTsr.exe" /T
taskkill /F /IM "UserOOBEBroker.exe" /T

REM del "%USERPROFILE%\OneDrive - Profinch Solutions Private Limited\Desktop\nulx" /s /f /q
del "%USERPROFILE%\AppData\Local\pip\cache" /s /f /q
rmdir "%TEMP%\" /q /s
rmdir "%TEMP%\*" /q /s

del "%USERPROFILE%\OneDrive - Profinch Solutions Private Limited\Pictures\Screenshots*" /s /f /q
del "%TEMP%\*.*" /s /f /q
@taskkill /f /im explorer.exe >nul
@start explorer.exe >nul
REM pause
