*** Settings ***
Library     SeleniumLibrary
Library     os
Library     Collections
Library     RequestsLibrary
Library    JSONLibrary

*** Variables ***
${BASE_URL}     https://api.restful-api.dev/
${END_URI}      objects/7

*** Test Cases ***
Get_countryInfo
        ${RESPONSE}=    GET     ${BASE_URL}${END_URI}

        ${JSON_OBJ}=    To Json    ${RESPONSE.content}

        #Single data validation
        ${Name_Value}=  Get Value From Json    ${JSON_OBJ}    $.name
        Log To Console    ${Name_Value[0]}
        Should Be Equal    ${Name_Value[0]}    Apple MacBook Pro 16

        #Single data validation
        ${Name_Value1}=  Get Value From Json    ${JSON_OBJ}    $.data.price
        Log To Console    ${Name_Value1[0]}
        ${Name_value1_int}=     Convert To String    ${Name_Value1[0]}
        Should Be Equal    ${Name_value1_int}    1849.99

        #Multiple data validation
        ${Data_Value}=  Get Value From Json    ${JSON_OBJ}    $.data
        Log To Console    ${Data_Value[0]}
        Should Contain Any    ${Data_Value[0]}    year  price   CPU model
        Should Not Contain Any    ${Data_Value[0]}      fghj   gfhk

