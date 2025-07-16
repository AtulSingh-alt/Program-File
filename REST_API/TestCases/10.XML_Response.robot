*** Settings ***
Library     XML
Library     os
Library     Collections
Library     RequestsLibrary

*** Variables ***
${BASE_URL}     https://mocktarget.apigee.net

*** Test Cases ***
TestCase1
        ${respose}=     Get     ${BASE_URL}/xml
        ${xml_string}=      Convert To String    ${respose.content}
        ${xml_obj}=     Parse Xml    ${xml_string}

        # checking single element value
        Element Text Should Be    ${xml_obj}    San Jose    .//city

        # cheking muliple values
        ${child_Elements}=      Get Child Elements    ${xml_obj}
        Log To Console    ${child_Elements}
        ${child_Elements1}=      Get Element Text    ${xml_obj}
        Log To Console    ${child_Elements1}
        Should Not Be Empty    ${child_Elements}

        ${city}=    Get Element Text    ${child_Elements[0]}
        ${firstName}=    Get Element Text    ${child_Elements[1]}
        ${lastName}=    Get Element Text    ${child_Elements[2]}
        ${state}=    Get Element Text    ${child_Elements[3]}

        Log To Console    ${city}
        Log To Console    ${firstName}
        Log To Console    ${lastName}
        Log To Console    ${state}