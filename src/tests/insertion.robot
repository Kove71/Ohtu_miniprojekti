*** Settings ***
Resource  resource.robot

*** Test Cases ***

Insert Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani
    Output Should Contain  item Tuntematon sotilas added

Insert Blog Readingtip
    Input Add Command
    Input Blog Type
    Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  title  Liikuntablogi
    Output Should Contain  item Endorfiineja added

Insert Podcast Readingtip
    Input Add Command
    Input Podcast Type
    Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri
    Output Should Contain  item Jäljillä added

Insert Video Readingtip
    Input Add Command
    Input Video Type
    Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial
    Output Should Contain  item How to Tie a Tie added

*** Keywords ***
