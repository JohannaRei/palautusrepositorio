*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  joha
    Set Password  johanna123
    Set Password Confirmation  johanna123
    Click Button  Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  jo
    Set Password  johanna123
    Set Password Confirmation  johanna123
    Click Button  Register
    Registration Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Invalid Password
    # salasana ei sisällä halutunlaisia merkkejä
    Set Username  johan
    Set Password  pitkasalasana
    Set Password Confirmation  pitkasalasana
    Click Button  Register
    Registration Should Fail With Message  Password must contain non-letter characters

Register With Valid Username And Too Short Password
    Set Username  johann
    Set Password  lyhyt!
    Set Password Confirmation  lyhyt!
    Click Button  Register
    Registration Should Fail With Message  Password must be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  johanna
    Set Password  johanna123
    Set Password Confirmation  johanna234
    Click Button  Register
    Registration Should Fail With Message  Password doesn't match confirmation

Login After Successful Registration
    Set Username  johannar
    Set Password  johanna123
    Set Password Confirmation  johanna123
    Click Button  Register
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  johannar
    Set Password  johanna123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  reiska
    Set Password  r
    Set Password Confirmation  r
    Click Button  Register
    Registration Should Fail With Message  Password must be at least 8 characters
    Click Link  Login
    Login Page Should Be Open
    Set Username  reiska
    Set Password  r
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Register Page
    Go To Starting Page
    Click Link  Register new user

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}