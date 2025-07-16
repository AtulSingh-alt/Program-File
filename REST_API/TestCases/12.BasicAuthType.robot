*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     http://restapi.demoqa.com
${end_uri}      /authentication/CheckForAuthentication/

*** Test Cases ***
BasicAuthTest
        ${auth}=        Create List     ToolsQA    TestPassword
        ${response}=        GET     ${base_url}${end_uri}      auth=${auth}
        Log To Console    ${response.content}
        
        #Validation
        Should Be Equal As Strings    ${response.status_code}    200
