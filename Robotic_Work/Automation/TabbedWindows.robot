*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TabbedWindow Test
        Open Browser    https://rahulshettyacademy.com/AutomationPractice/      chrome
        Click Element    xpath://*[@id="opentab"]
        Switch Window    title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
        Click Element    //*[@id="navbarSupportedContent"]/ul/li[5]/a
        Input Text    name    atatul
        Sleep    3
        Close All Browsers
