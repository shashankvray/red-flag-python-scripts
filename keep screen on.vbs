Set wsc = WScript.CreateObject( "WScript.Shell" ) 

Do Until Hour(Now()) = 18
    WScript.Sleep(30000)
    wsc.SendKeys("{F13}")
Loop 