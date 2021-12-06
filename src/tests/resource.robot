*** Settings ***

Library  ../ReadingtipLibrary.py


*** Keywords ***

Input Add Command
    Input  a

Input View Command
    Input  v

Input Clear Command
    Input  c

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
    [Arguments]  ${name}  ${author}  ${title}  ${description}
    Input  ${name}
    Input  ${author}
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
