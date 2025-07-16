*** Settings ***
Documentation     DropDownAlert
Library     SeleniumLibrary


*** Variables ***
${url}      https://training.qaonlinetraining.com/testPage.php
${browser}  Chrome

*** Test Cases ***
RadioButton and CheckBox
    Perform Click on Button

Dropdown elements
    Select Value

Alert Test
    Alert click

*** Keywords ***
Perform Click on Button
    Open Browser    ${url}      ${browser}
    Maximize Browser Window
    Click Element    xpath:/html/body/form/input[5]
    Sleep    10
    Click Element    xpath:/html/body/form/input[9]

Select Value
    Select From List By Label    country    Ethiopia
    Sleep    10
    Click Element    name:submit

Alert click
    Click Element    id:alert
    Handle Alert    accept
    Sleep    10
    Click Element    id:confirm
    Handle Alert    DISMISS
    Sleep    10
