*** Settings ***

Library  ../ReadingtipLibrary.py


*** Keywords ***

Input Add Command
    Input  a

Input View Command
    Input  v

Input Clear Command
    Input  c

Input Exit Command
    Input  q

Creating Readingtip
    [Arguments]  ${readingtip}
    Input Add Command
    Input  ${readingtip}
    Run Application
