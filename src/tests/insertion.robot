*** Settings ***
Resource  resource.robot
Test Setup  Insert Initial Readingtip

*** Test Cases ***

Insert Readingtip
    Creating Readingtip  Ylioppilaslehti 2/2018
    Last Output Should Contain  item Ylioppilaslehti 2/2018 added

View All Items When One Readingtip Added 
    Input View Command
    Run Application
    Last Output Should Contain  item Vakooja ja petturi added

Readingtip Removal When Two Readingtip Added
    Creating Readingtip  Ylioppilaslehti 2/2018
    Creating Readingtip  Kirjanen
    Input Clear Command
    Run Application
    Database Must Be Empty

*** Keywords ***
Insert Initial Readingtip
    Creating Readingtip   Vakooja ja petturi
