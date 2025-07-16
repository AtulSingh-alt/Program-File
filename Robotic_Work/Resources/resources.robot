*** Settings ***
Library     SeleniumLibrary



*** Keywords ***
LaunchBrowser
        [Arguments]         ${appurl1}  ${appbrowser}
        Open Browser        ${appurl1}  ${appbrowser}
        Maximize Browser Window
        ${title}=       Get Title
        [Return]        ${title}