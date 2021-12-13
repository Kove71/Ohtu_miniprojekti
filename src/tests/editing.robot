*** Settings ***
Resource  resource.robot

*** Test Cases ***

Edit Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani

    Change Book Name  Asdf    
    View Books
    Output Should Contain  Name: Asdf

    Change Book Author  Asdf
    View Books
    Output Should Contain  Author: Asdf

    Change Book ISBN  Asdf
    View Books
    Output Should Contain  ISBN: Asdf

    Change Book Description  Asdf
    View Books
    Output Should Contain  Description: Asdf

Edit Blog Readingtip
    Input Add Command
    Input Blog Type
    Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  title  Liikuntablogi

    Change Blog Name  Asdf
    View Blogs
    Output Should Contain  Name: Asdf

    Change Blog Author  Asdf
    View Blogs
    Output Should Contain  Author: Asdf

    Change Blog URL  Asdf
    View Blogs
    Output Should Contain  URL: Asdf

    Change Blog Description  Asdf
    View Blogs
    Output Should Contain  Description: Asdf


Edit Podcast Readingtip
    Input Add Command
    Input Podcast Type
    Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri

    Change Podcast Name  Asdf
    View Podcasts
    Output Should Contain  Name: Asdf

    Change Podcast Episode  Asdf
    View Podcasts
    Output Should Contain  Episode: Asdf

    Change Podcast URL  Asdf
    View Podcasts
    Output Should Contain  URL: Asdf

    Change Podcast Description  Asdf
    View Podcasts
    Output Should Contain  Description: Asdf

Edit Video Readingtip
    Input Add Command
    Input Video Type
    Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial

    Change Video Name  Asdf
    View Videos
    Output Should Contain  Name: Asdf

    Change Video URL  Asdf
    View Videos
    Output Should Contain  URL: Asdf
    
    Change Video Channel  Asdf
    View Videos
    Output Should Contain  Channel: Asdf

    Change Video Description  Asdf
    View Videos
    Output Should Contain  Description: Asdf

*** Keywords ***
