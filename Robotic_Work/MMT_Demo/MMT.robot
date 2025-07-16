*** Settings ***
Library     SeleniumLibrary
Library     Collections
Library     String

*** Variables ***
${BASE_URL}     https://www.makemytrip.com/
${BROWSER}      Chrome


*** Test Cases ***
MMT Flow
    Open Browser        ${BASE_URL}     ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    .5
    Set Selenium Timeout    10

    Wait Until Element Is Visible    xpath=//span[contains(@class,'commonModal__close')]
    Click Element    xpath=//span[contains(@class,'commonModal__close')]

    Wait Until Element Is Visible    xpath=(//span[text() = 'Flights'])[1]
    Click Element    xpath=(//span[text() = 'Flights'])[1]

    Click Element    xpath=(//span[contains(@class,'tabsCircle appendRight5')])[2]
    Click Element    xpath=(//span[contains(@class,'tabsCircle appendRight5')])[1]

    Click Element    xpath=(//input[contains(@type,'text')])[1]
    Wait Until Element Is Visible    xpath=(//input[contains(@type,'text')])[1]
    Input Text    xpath=//input[contains(@placeholder,'From')]    Delhi
    Wait Until Element Is Visible    xpath=//*[@id="react-autowhatever-1-section-0-item-0"]/div/div/p[1]/span[1]/span
    Click Element    xpath=//*[@id="react-autowhatever-1-section-0-item-0"]/div/div/p[1]/span[1]/span

    Click Element    xpath=(//input[contains(@type,'text')])[2]
    Wait Until Element Is Visible    xpath=(//input[contains(@type,'text')])[2]
    Input Text    xpath=//input[contains(@placeholder,'To')]    Varanasi
    Wait Until Element Is Visible    xpath=//*[@id="react-autowhatever-1-section-0-item-0"]/div/div/p[1]/span[1]
    Click Element    xpath=//*[@id="react-autowhatever-1-section-0-item-0"]/div/div/p[1]/span[1]

    Click Element    xpath=//*[@id="top-banner"]/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[2]/div

    Click Element    xpath=//a[contains(@class,'primaryBtn font24 latoBold widgetSearchBtn ')]
    Sleep    5











