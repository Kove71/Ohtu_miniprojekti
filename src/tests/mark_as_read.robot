*** Settings ***
Resource  resource.robot

*** Test Cases ***

Mark Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani
    
    Mark As Read  1

    View Books
    Check Tip Is Read

Mark Blog Readingtip
    Input Add Command
    Input Blog Type
    Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  title  Liikuntablogi

    Mark As Read  1
    View Blogs
    Check Tip Is Read

Mark Podcast Readingtip
    Input Add Command
    Input Podcast Type
    Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri

    Mark As Read  1
    View Podcasts
    Check Tip Is Read

Mark Video Readingtip
    Input Add Command
    Input Video Type
    Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial

    Mark As Read  1
    View Videos
    Check Tip Is Read
    
*** Keywords ***
