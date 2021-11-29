*** Settings ***
Resource  resource.robot

*** Test Cases ***

Insert Readingtip
    Input Add Command
    Input Credentials  Ylioppilaslehti 2/2018
    Application Runs With Given Commands
    Last Output Should Contain  item Ylioppilaslehti 2/2018 added

View All Items When Two Readingtips Added
    Input Add Command
    Input Credentials  Kirjanen
    Input Add Command
    Input Credentials  Vakooja ja petturi 
    Input View Command
    Application Runs With Given Commands
    Last Output Should Contain  Vakooja ja petturi

Clear All Readingtips
    Creating Readingtip  Ylioppilaslehti 2/2018
    Creating Readingtip  Kirjanen
    Input Clear Command
    Application Runs With Given Commands
    Database Must Be Empty

Insert Invalid Command
    Input  virheellinenkomento
    Application Runs With Given Commands
    Last Output Should Contain  command not found


*** Keywords ***
