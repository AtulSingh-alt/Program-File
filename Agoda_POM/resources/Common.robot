*** Settings ***
Library    SeleniumLibrary
Resource    ../variables/variables.robot

*** Keywords ***
Open Agoda
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window

Close App
    Close Browser