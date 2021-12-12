*** Settings ***

Library  ../ReadingtipLibrary.py


*** Keywords ***

Input Add Command
    Input  a

Input View Command
    Input  v

Input Clear Command
    Input  c

Input Edit Command
    Input  e

Input Exit Command
    Input  q

Input Book Type
    Input  1

Input Blog Type
    Input  2

Input Podcast Type
    Input  3

Input Video Type
    Input  4

Create New Book
    [Arguments]  ${name}  ${author}  ${isbn}  ${description}
    Input  ${name}
    Input  ${author}
    Input  ${isbn}
    Input  ${description}
    Run Application

Create New Blog
    [Arguments]  ${name}  ${author}  ${url}  ${title}  ${description}
    Input  ${name}
    Input  ${author}
    Input  ${url}
    Input  ${title}
    Input  ${description}
    Run Application

Create New Podcast
    [Arguments]  ${name}  ${episode}  ${url}  ${description}
    Input  ${name}
    Input  ${episode}
    Input  ${url}
    Input  ${description}
    Run Application

Create New Video
    [Arguments]  ${name}  ${url}  ${channel}  ${description}
    Input  ${name}
    Input  ${url}
    Input  ${channel}
    Input  ${description}
    Run Application

View Books
    Input View Command
    Input Book Type
    Run Application

View Blogs
    Input View Command
    Input Blog Type
    Run Application

View Podcasts
    Input View Command
    Input Podcast Type
    Run Application

View Videos
    Input View Command
    Input Video Type
    Run Application

View All
    Input View Command
    Input  5
    Run Application

Change Book Name
    [Arguments]  ${name}
    Input Edit Command
    Input Book Type
    Input  1
    Input  1
    Input  ${name}
    Run Application

Change Book Author
    [Arguments]  ${author}
    Input Edit Command
    Input Book Type
    Input  1
    Input  2
    Input  ${author}
    Run Application

Change Book ISBN
    [Arguments]  ${ISBN}
    Input Edit Command
    Input Book Type
    Input  1
    Input  3
    Input  ${ISBN}
    Run Application

Change Book Description
    [Arguments]  ${description}
    Input Edit Command
    Input Book Type
    Input  1
    Input  4
    Input  ${description}
    Run Application


Change Blog Name
    [Arguments]  ${name}
    Input Edit Command
    Input Blog Type
    Input  1
    Input  1
    Input  ${name}


Change Blog Author
    [Arguments]  ${author}
    Input Edit Command
    Input Blog Type
    Input  1
    Input  2
    Input  ${author}


Change Blog URL
    [Arguments]  ${URL}
    Input Edit Command
    Input Blog Type
    Input  1
    Input  3
    Input  ${URL}


Change Blog Description
    [Arguments]  ${description}
    Input Edit Command
    Input Blog Type
    Input  1
    Input  4
    Input  ${description}


Change Podcast Name
    [Arguments]  ${name}
    Input Edit Command
    Input Podcast Type
    Input  1
    Input  1
    Input  ${name}


Change Podcast Episode
    [Arguments]  ${episode}
    Input Edit Command
    Input Podcast Type
    Input  1
    Input  2
    Input  ${episode}


Change Podcast URL
    [Arguments]  ${URL}
    Input Edit Command
    Input Podcast Type
    Input  1
    Input  3
    Input  ${URL}


Change Podcast Description
    [Arguments]  ${description}
    Input Edit Command
    Input Podcast Type
    Input  1
    Input  4
    Input  ${description}



Change Video Name
    [Arguments]  ${name}
    Input Edit Command
    Input Video Type
    Input  1
    Input  1
    Input  ${name}


Change Video URL
    [Arguments]  ${URL}
    Input Edit Command
    Input Video Type
    Input  1
    Input  2
    Input  ${URL}


Change Video Channel
    [Arguments]  ${channel}
    Input Edit Command
    Input Video Type
    Input  1
    Input  3
    Input  ${channel}


Change Video Description
    [Arguments]  ${description}
    Input Edit Command
    Input Video Type
    Input  1
    Input  4
    Input  ${description}