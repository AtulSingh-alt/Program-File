*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://api.restful-api.dev/
${end_uri}      objects



*** Test Cases ***
Registration Missing Data
    ${body}=    Create Dictionary   name=Apple MacBook Pro 16   year=2019
    ${header}=  Create Dictionary   Content-Type=application/json
    ${response}=    POST    ${base_url}${end_uri}   json=${body}    headers=${header}

    Log To Console    ${response.status_code}
    Log To Console    ${response.content}

    #Validation
    ${code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${code}      200

    ${res_body}=    Convert To String    ${response.content}
    Should Contain    ${res_body}   MacBook