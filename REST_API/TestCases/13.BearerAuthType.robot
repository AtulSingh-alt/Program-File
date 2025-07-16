*** Settings ***
Library     RequestsLibrary
Library     Collections
Library     OperatingSystem


*** Variables ***
${base_url}     https://certtransaction.elementexpress.com
${bearerToken}      "Bearer hj345jhk345kjh345hjk4tjhk435b"


*** Test Cases ***
BearerAuthTest
        ${headers}      Create Dictionary   Authorization=${bearerToken}    Content-Type=text/xml
        ${req_body}=    Get File    C:/Program Files/Python313/breakfast_menu.xml
        ${response}=    POST    ${base_url}     data=${req_body}    headers=${headers}
        Log To Console    ${response.status_code}
        Log To Console    ${response.content}

