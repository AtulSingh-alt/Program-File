*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://reqres.in
${end_uri}      2

*** Test Cases ***
TestDetails
    ${response}=    GET     ${base_url}/api/users/${end_uri}

    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    Log To Console    ${response.headers}
    
    #Validation
    ${status_code}=     Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200
    
    ${body}=        Convert To String    ${response.content}
    Should Contain    ${body}    Janet
    
    ${header_value}=    Get From Dictionary    ${response.headers}    Transfer-Encoding
    Should Be Equal    ${header_value}    chunked
