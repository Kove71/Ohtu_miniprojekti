*** Settings ***
Resource  resource.robot

*** Test Cases ***

Remove Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani
    Remove Item  1

    Clear Output

    View Books
    Output Should Not Contain  Name: Tuntematon sotilas
    Output Should Not Contain  Author: Väinö Linna
    Output Should Not Contain  ISBN: 9789510425459
    Output Should Not Contain  Description: sotaromaani


Remove Blog Readingtip
    Input Add Command
    Input Blog Type
    Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  title  Liikuntablogi
    Remove Item  1

    Clear Output

    View Blogs
    Output Should Not Contain  Name: Endorfiineja
    Output Should Not Contain  Author: Kirsi
    Output Should Not Contain  URL: https://kirsberry.blogspot.com
    Output Should Not Contain  Description: Liikuntablogi

Remove Podcast Readingtip
    Input Add Command
    Input Podcast Type
    Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri
    Remove Item  1

    Clear Output

    View Podcasts
    Output Should Not Contain  Name: Jäljillä
    Output Should Not Contain  Episode: Jessica Johnson
    Output Should Not Contain  URL: https://www.spotify.com
    Output Should Not Contain  Description: Katoamistapausmysteeri

View Video Readingtip
    Input Add Command
    Input Video Type
    Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial
    Remove Item  1

    Clear Output

    View Videos
    Output Should Not Contain  Name: How to Tie a Tie
    Output Should Not Contain  URL: https://www.youtube.com/watch?v=xAg7z6u4NE8
    Output Should Not Contain  Channel: tiehole
    Output Should Not Contain  Description: how to tie a tie tutorial

*** Keywords ***
