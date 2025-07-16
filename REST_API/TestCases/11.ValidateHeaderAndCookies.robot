*** Settings ***
Library     RequestsLibrary
Library     Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}     https://reqres.in/api/

*** Test Cases ***
TestHeaders
        ${response}=    Get     ${BASE_URL}users/2
        
        Log To Console    ${response.headers}

        #Capture specifc key & value
        ${contentTypeValue}=     Get From Dictionary    ${response.headers}    Content-Type
        Log To Console    ${contentTypeValue}
        ${X_Frame_OptionsValue}=     Get From Dictionary    ${response.headers}    X-Frame-Options
        Log To Console    ${X_Frame_OptionsValue}

TestCookies
        ${response}=        GET     ${BASE_URL}users/2

        Log To Console    ${response.cookies}

        #Capture specific key & value
#        ${cookieValue}=     Get From Dictionary    ${response.cookies}  fygu
#        Log To Console    ${cookieValue}
