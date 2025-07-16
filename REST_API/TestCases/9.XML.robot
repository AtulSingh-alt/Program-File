*** Settings ***
Library     XML
Library     os
Library     Collections

*** Test Cases ***
XML Validation
        ${xml_obj}=     Parse Xml    C:/Program Files/Python313/breakfast_menu.xml

        #Validation
        #Val1- Check the Single Element Value
        #Approach1
        ${Food_first_name}=     Get Element Text    ${xml_obj}      .//food[3]/name
        Log To Console    ${Food_first_name}
        Should Be Equal    ${Food_first_name}    Berry-Berry Belgian Waffles

        #Approach2
        ${Food_first_name1}=    Get Element    ${xml_obj}       .//food[3]/name
        Should Be Equal    ${Food_first_name1.text}    Berry-Berry Belgian Waffles

        #Approach3
        Element Text Should Be    ${xml_obj}    Berry-Berry Belgian Waffles     .//food[3]/name

        #Validation 2- Check number of elements
        ${count}=   Get Element Count    ${xml_obj}     .//food
        Log To Console    ${count}
        Should Be Equal As Integers    ${count}    5

        #Validation 3- Check attribute presence
#        Element Attribute Should Be    ${xml_obj}    id    fhhg        .//food[4]

        #Validation 4- Check values of child elements
        ${child_element}=   Get Child Elements    ${xml_obj}    .//food[1]
        Should Not Be Empty    ${child_element}

        ${Ele_name}=    Get Element Text    ${xml_obj}      .//food[1]
        Log To Console    ${Ele_name}
#        ${fname}=   Get Element Text    ${Ele_name[0]}
#        ${lname}=   Get Element Text    ${Ele_name[1]}
#        ${title_name}=   Get Element Text    ${Ele_name[2]}
#
#        Log To Console    ${fname}
#        Log To Console    ${lname}
#        Log To Console    ${title_name}


