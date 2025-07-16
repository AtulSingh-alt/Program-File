*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://dummy.restapiexample.com/public/api/
${end_uri}      v1/update/21


*** Test Cases ***
Registration Missing Data
    ${body}=    Create Dictionary   name=test   salary=123  age=23
    ${header}=  Create Dictionary   Content-Type=application/json   Accept=*/*
    ${response}=    PUT     ${base_url}${end_uri}   json=${body}    headers=${header}

    Log To Console    ${response.status_code}
    Log To Console    ${response.content}

    #Validation
    ${code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${code}      200

    ${res_body}=    Convert To String    ${response.content}
    Should Contain    ${res_body}   test