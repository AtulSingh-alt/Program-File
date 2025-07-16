*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://reqres.in/api/
${details}      users


*** Test Cases ***
#Registration_data
#    Create Session    mysession    ${base_url}
#    ${body}=    Create Dictionary   name=morpheus   job=leader
#    ${header}=  Create Dictionary   Content-Type=application/json   x-api-key=reqres-free-v1
#    ${response}=    Post Request    mysession    ${details}     data=${body}    headers=${header}
#
#    Log To Console    ${response.status_code}
#    Log To Console    ${response.content}
#
#    #Validation
#    ${code}=    Convert To String    ${response.status_code}
#    Should Be Equal    ${code}    201
#
#    ${res_body}=    Convert To String    ${response.content}
#    Should Contain    ${res_body}   leader

Registration_data
    ${body}=    Create Dictionary   name=morpheus   job=leader
    ${header}=  Create Dictionary   Content-Type=application/json   x-api-key=reqres-free-v1
    ${response}=    POST    ${base_url}${details}     json=${body}    headers=${header}

    Log To Console    ${response.status_code}
    Log To Console    ${response.content}

    #Validation
    ${code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${code}    201

    ${res_body}=    Convert To String    ${response.content}
    Should Contain    ${res_body}   leader



