*** Settings ***
Resource  resource.robot

*** Test Cases ***

Mark Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani
    
    Mark As Read  1

    View Books
    Output Should Contain  Read:

# View Blog Readingtip
#     Input Add Command
#     Input Blog Type
#     Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  title  Liikuntablogi

#     View Blogs
#     Output Should Contain  Name: Endorfiineja
#     Output Should Contain  Author: Kirsi
#     Output Should Contain  URL: https://kirsberry.blogspot.com
#     Output Should Contain  Description: Liikuntablogi

# View Podcast Readingtip
#     Input Add Command
#     Input Podcast Type
#     Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri

#     View Podcasts
#     Output Should Contain  Name: Jäljillä
#     Output Should Contain  Episode: Jessica Johnson
#     Output Should Contain  URL: https://www.spotify.com
#     Output Should Contain  Description: Katoamistapausmysteeri

# View Video Readingtip
#     Input Add Command
#     Input Video Type
#     Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial

#     View Videos
#     Output Should Contain  Name: How to Tie a Tie
#     Output Should Contain  URL: https://www.youtube.com/watch?v=xAg7z6u4NE8
#     Output Should Contain  Channel: tiehole
#     Output Should Contain  Description: how to tie a tie tutorial

*** Keywords ***
