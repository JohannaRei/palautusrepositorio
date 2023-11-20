*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  johanna  johanna123

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  johanna  johanna234
    Output Should Contain  User with username johanna already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  jo  johanna123
    Output Should Contain  Username must be at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  johanna!  johanna123
    Output Should Contain  Username must only contain letters

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  johanna  johanna
    Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  johanna  johannajohanna
    Output Should Contain  Password must contain non-letter characters