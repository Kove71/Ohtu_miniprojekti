*** Settings ***
Resource  resource.robot

*** Test Cases ***

Insert Book Readingtip
    Input Add Command
    Input Book Type
    Create New Book  Tuntematon sotilas  Väinö Linna  9789510425459  sotaromaani
    Output Should Contain  \nitem Type: Book\nName: Tuntematon sotilas\nAuthor: Väinö Linna\nISBN: 9789510425459\nDescription: sotaromaani\nRead: No\n added \n

Insert Blog Readingtip
    Input Add Command
    Input Blog Type
    Create New Blog  Endorfiineja  Kirsi  https://kirsberry.blogspot.com  Liikuntablogi
    Output Should Contain  \nitem Type: Blog\nName: Endorfiineja\nAuthor: Kirsi\nTitle: Liikuntablogi\nURL: https://kirsberry.blogspot.com\nDescription: q\nRead: No\n added \n


Insert Podcast Readingtip
    Input Add Command
    Input Podcast Type
    Create New Podcast  Jäljillä  Jessica Johnson  https://www.spotify.com  Katoamistapausmysteeri
    Output Should Contain  \nitem Type: Podcast\nName: Jäljillä\nEpisode: Jessica Johnson\nURL: https://www.spotify.com\nDescription: Katoamistapausmysteeri\nRead: No\n added\n

Insert Video Readingtip
    Input Add Command
    Input Video Type
    Create New Video  How to Tie a Tie  https://www.youtube.com/watch?v=xAg7z6u4NE8  tiehole  how to tie a tie tutorial
    Output Should Contain  \nitem Type: Video\nName: How to Tie a Tie\nURL: https://www.youtube.com/watch?v=xAg7z6u4NE8\nChannel: tiehole\nDescription: how to tie a tie tutorial\nWatched: No\n added\n

*** Keywords ***
