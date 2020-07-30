# Monitoring Script
Python script to do some monitoring, updates and send emails with status

# Introduction
This script allows you to check if java exists and get the version if so, otherwise, install the version wanted and send emails with different status along the verification;

# Development environment
* Python = 3.7
* Os covered : Linux

# How to run locally
On a terminal run 
```
python monitor.py
```
# Functionalities
* Check java exist
* Check java version
* Download and install java (creating the different variables as alias)
* Send email with status
* For update the version if not existing, the download and instal functionnality with the version desired is considered     
  To make full use of the script below, make sure that you include all the required parameters:
    * The url parameters for the download (packages to install, version, update, b, auth == token)
    * The sender of the email, the host and the port (if available), the recipients and the message to attach     
    ### N.B : 
    If you're using the gmail server or any other protected server make sure that you allow the secure less applications since 'smtp' is considered as a secure less one

# Note
The script is easily scalable to cover different os and architectures, to adapt it to a different os : this one should be considered in the condition of the os and the commands should be adapted if different.
