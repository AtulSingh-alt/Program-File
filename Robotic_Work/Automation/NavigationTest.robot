*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
Navigation Test
        Open Browser    https://www.google.com      chrome
        Maximize Browser Window
        ${loc}=     Get Location
        Log To Console    ${loc}
        Sleep    3

        Go To    https://www.bing.com/
        Maximize Browser Window
        ${loc}=     Get Location
        Log To Console    ${loc}
        Sleep    3

        Go Back
        Maximize Browser Window
        ${loc}=     Get Location
        Log To Console    ${loc}
        Sleep    3
