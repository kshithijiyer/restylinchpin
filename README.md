# restylinchpin
flask based RESTful API wrapper built around project linchpin

# Table Of Contents
- [Overview](#overview)
- [Deployment](#deployment)
- [Documenation (In progress)](#documentation)

# Overview
HTTP RESTful API.

Requests pass data via JSON encoded bodies except for GET requests where data will be passed via URL and excecute them on linchpin Command Line Interface to provision workspaces and return a JSON response to the user.

A user can currently make use of following supported features:
- <b> Create Workspaces :</b> Users can create a new worskpace locally.
- <b> List Workspaces :</b> Users can list all existing workspace within a config directory.
- <b> Delete Workspaces :</b> Users can delete workspace by name.
- <b> Fetch Workspaces from a remote URL :</b> Users can fetch remote workspaces from git or web directory locally.
- <b> Provision workspaces :</b> Users can provision workspaces across multiple cloud providers.
- <b> Destroy Workspaces :</b> Users can teardown the resources provisioned after using them.

## User Management
api_key based authentication for user operations

<b> creating users </b> <br>
endpoint:<br>
/users <br>
methodtype: POST <br>
request: <br>
{<br>
  "username":"username", <br>
  "password":"password", <br>
  "email":"email" <br>
}<br>
response: <br>
{<br>
  username=username, <br>
  admin=boolean indicating created as admin user or not <br>
  email=email,<br>
  status="username created successfully" <br>
}<br>

<b> Login </b> <br>
endpoint:<br>
/login <br>
User has to send a basic authentication header with username and password generated above, an autogenerated (hashed) api_key will be returned to the user for resource access.<br>
Response:<br>
{<br>
"api_key":"api_key value"<br>
}<br>
This api_key will be verified by passing a key:api_key and value: api_key value obtained above,in the request headers during each of the API calls including user and workspace actions to grant resource access by determining the access rights of the current user. Admin users can access all resources whereas other resources are only accessible to the owner of that resource.

<b> Reset api key </b> <br>
methodType: POST <br>
endpoint: <br>
/api/v1.0/users/username/reset <br>
Response: {api_key= value, message = "reset successfully"}<br>

<b>listing users</b> <br>
<b>One user: </b><br>
(Admin user only) <br>
endpoint:<br>
/users/username<br>
methodType: GET<br>
response:<br>
{<br>
username=username,<br>
api_key=api_key,<br>
admin=boolean indicating created as admin user or not<br>
}<br>

<b>All users:</b><br>
(Admin user only)<br>
endpoint:<br>
/users<br>
methodType: GET<br>
response:<br>
{<br>
[user1: {username: username, password: password(hashed), api_key:api_key} ] <br>
status=200 OK<br>
}<br>

<b>Promote users to admin status</b><br>
(Admin user only)<br>
endpoint:<br>
methodType: PUT<br>
/api/v1.0/users/username/promote<br>
Response: {user has been promoted as an admin}<br>

<b>Update user fields</b><br>
endpoint:<br>
methodType: PUT<br>
/api/v1.0/users/username<br>
request:<br>
{
"username":"username",<br>
"password":"password",<br>
"email":"email"<br>
}<br>
response:<br>
{
username=username,<br>
password= hashed_password,<br>
email=email,<br>
status=OK<br>
}<br>


## Linchpin Project
LinchPin is a simple cloud orchestration tool. Its intended purpose is managing cloud resources across multiple infrastructures. These resources can be provisioned, decommissioned, and configured all using declarative data and a simple command-line interface.

Refer to Linchpin Repository for detailed information: 
<a>https://github.com/CentOS-PaaS-SIG/linchpin</a>

# Deployment
restylinchpin will be deployed and available on Openshift.<br>
Start using restylicnhpin with pypi: <a href="https://pypi.org/project/restylinchpin/">pip install restylinchpin</a>

# Documenation (In progress)
Swagger <br>
ReadTheDocs