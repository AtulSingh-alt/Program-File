*** Settings ***
Library     JSONLibrary
Library     os
Library     Collections


*** Test Cases ***

TestCase1:
        ${json_obj}=        Load Json From File       C:/Program Files/Python313/jsondata.json
        ${name_value}=      Get Value From Json         ${json_obj}    $.array[1].dictionary.b
        
#        Log To Console    ${name_value}
        Should Be Equal    ${name_value[0]}    Butterfly

        ${name_value}=      Get Value From Json         ${json_obj}    $.array[1].key
        ${name_value_str}=     Convert To String    ${name_value[0]}
        Should Be Equal    ${name_value_str}        2