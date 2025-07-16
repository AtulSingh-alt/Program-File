*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
#For Loop1
#        :FOR    ${i}    IN RANGE 1 10
#            Log To Console    %{i}

#For Loop2
#        :FOR    ${i}    IN  1 2 3 4 5 6
#            Log To Console    %{i}

#For Loop3withList
#        @{items}   create list     1   2   3   4   5
#        :FOR     ${i}    IN  @{items}
#            Log To Console    ${i}

#For Loop4
#        :FOR    ${i}    IN  john    david   smith   scott
#            Log To Console    %{i}

#For Loop5
#        @{nameslist}    Create List     john    david   smith   scott
#        :FOR    ${i}    IN  @{nameslist}
#            Log To Console    ${i}

ForLoop6withExit
    @{items}       Create List      1   2   3   4   5
    FOR    ${i}    IN    @{items}
        Log    ${i}

    END
        Log To Console    ${i}
            Exit For Loop If    ${i}==3