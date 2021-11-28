*** Settings ***

Resource  resource.robot


*** Test Cases ***
#Ensimmäinen testitapaus ei suorita vielä mitään
Insert With Valid Credentials 
    Input  value
    Output Should Contain  true

