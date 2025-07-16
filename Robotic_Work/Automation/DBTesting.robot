*** Settings ***
Library     DatabaseLibrary
Library     OperatingSystem

Suite Setup         Connect to Database     pymysql     ${DBName}   ${DBUser}   ${DBPass}   ${DBHost}   ${DBPort}
Suite Teardown      Disconnect from database

*** Variables ***
${DBName}      mydb
${DBUser}       root
${DBPass}       root
${DBHost}       127.0.0.1
${DBPort}       3306


*** Test Cases ***
Create person table
    ${output}=  Execute SQL String      Create table person(id integer,first_name varchar(20),Last_name varchar(20));
    Log To Console    ${output}
    Should Be Equal As Strings    ${output}     None

Inserting Data in person Table
    # For single Record
    ${output}=  Execute SQL String      Insert into person values(101,"John","canady");

    # for Multiple records
    #${output}= Execute SQL Script   ./folder_name/file_name
    Log To Console    ${output}
    Should Be Equal As Strings    ${output}     None

Check David record present in person Table
    check if exists in database     select id from mydb.person where first_name="David";

Check Jio record Not present in Person Table
    check if not exists in database     select id from mydb.person where first_name="Jio";

Check Person Table exists in mydb database
    table must exist    person

Verify Row Count is Zero
    row count is 0  SELECT * FROM mydb.person WHERE first_name = 'xyz';

Verify Row Count is Equal to Some Value
    row count is equal to x     SELECT * FROM mydb.person WHERE first_name = 'David';   1

Verify Row Count is Greater than Some Value
    row count is greater than x     SELECT * FROM mydb.person   WHERE first_name =  'David';    0

Verify Row Count is less than Some Value
    row count is less than      SELECT * FROM mydb.person   WHERE first_name =  'David';    5

Update record in person table
    ${output}=  Execute SQL String  Update mydb.person  set first_name = "JIO" where id=104;
    Log To Console    ${output}
    Should Be Equal As Strings    ${output}    None

Retrieve Records from Person Table
    @{queryResults}=    query   Select *    from mydb.person;
    Log To Console  many    @{queryResults}

Delete Records from person table
    ${output}=  Execute SQL String      Delete from mydb.person;
    Should Be Equal As Strings    ${output}    None
