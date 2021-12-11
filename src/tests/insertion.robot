*** Settings ***
Resource  resource.robot

*** Test Cases ***

Insert Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani
    Output Should Contain  \nitem Tuntematon sotilas added \n

Insert Blog Readingtip
    Input Add Command
    Input Blog Type
    Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  Liikuntablogi
    Output Should Contain  \nitem Endorfiineja added \n

Insert Podcast Readingtip
    Input Add Command
    Input Podcast Type
    Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri
    Output Should Contain  \nitem Jäljillä added\n

Insert Video Readingtip
    Input Add Command
    Input Video Type
    Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial
    Output Should Contain  \nitem How to Tie a Tie added\n

*** Keywords ***
