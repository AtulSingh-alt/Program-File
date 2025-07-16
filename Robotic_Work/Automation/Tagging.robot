*** Settings ***



*** Test Cases ***
TC1 User RegistrationTest
    [Tags]      sanity
    Log To Console    This is user reg test
    Log To Console    user reg test is over
TC2 LoginTest
    [Tags]      regression
    Log To Console    This is login test
    Log To Console    Login test is over
TC3 Change user settings
    [Tags]      regression
    Log To Console    This is changing user settings test
    Log To Console    Change user settings test is over
TC4 Logout Test
    [Tags]      sanity
    Log To Console    This is logout test
    Log To Console    logout test is over

#  cmd for run -> robot --include=sanity Tagging.robot or robot -i sanity -i regression Tagging.robot or robot -e regression tagging.robot
