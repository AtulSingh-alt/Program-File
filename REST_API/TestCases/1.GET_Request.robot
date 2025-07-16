*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://gorest.co.in
${details}      users


*** Test Cases ***
Get_users_details
    #Create Session    myssion    ${base_url}        verify=True
    #${response}=    GET On Session    myssion    /public/v2/${details}
    ${response}=    GET    ${base_url}/public/v2/${details}

#    Log To Console    ${response.status_code}
#    Log To Console    ${response.content}
#    Log To Console    ${response.headers}

    #Validation
    ${status_code}=     convert to string   ${response.status_code}
    Should Be Equal    ${status_code}    200

    ${body}=        convert to string   ${response.content}
    Should Contain    ${body}    7969797

    ${header_Connection_value}=      Get From Dictionary    ${response.headers}    Connection
    Should Be Equal    ${header_Connection_value}    keep-alive



*** Keywords ***