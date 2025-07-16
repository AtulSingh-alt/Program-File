*** Settings ***
Documentation       Test case to execute the login process
Library     SeleniumLibrary

*** Variables ***
${Url}      https://demo.itlearn360.com/
${Browser}  Chrome


*** Keywords ***
Open the Url
    Open Browser    ${Url}    ${Browser}