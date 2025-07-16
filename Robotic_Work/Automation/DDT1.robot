*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/login_resources.robot
Suite Setup     Open my Browser
Suite Teardown  Close Browsers
Test Template   Invalid login

*** Test Cases ***          username                    password
Right user empty pwd        admin@yourstore.com         ${EMPTY}
Right user wrong pwd        admin@yourstore.com         xyz
Wrong user right pwd        admin@yourstore.com         admin
Wrong user empty pwd        adm@yourstore.com           ${EMPTY}
Wrong user wrong pwd        adm@yourstore.com           xyz




*** Keywords ***
Invalid login
    [Arguments]     ${username}     ${password}
    Input Username    ${username}
    Input pwd    ${password}
    click login button
    Error message should be visible