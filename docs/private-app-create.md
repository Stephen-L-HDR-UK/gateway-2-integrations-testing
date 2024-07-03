## Glossary

|Term|Description|
|------|-------------|
|Private App|An application/service/ETL tool that is developed by a user who wants to be able to programmatically interact with the Gateway. |
|AppID and ClientID |Tokens that are generated when creating a new Private App. Each Private App will have a unique AppID and ClientID that needs to be sent with each API request to authenticate and approve the action. |
|Team Admin/Developer |A role that can be assigned to a user when they are part of a ‘team’ on the Gateway. Please see the documentation [here](https://www.healthdatagateway.org/about/how-to-manage-teams-on-the-gateway) on roles and permissions on the Gateway. |
|Authenticated API Endpoint |While a lot of the Gateway APIs are accessible without authentication, any endpoint changing data requires authentication. The ClientID acts as an authentication token. |

## Introduction

The Private Apps feature enables developers to create a Private App and corresponding ClientID which is used as a token to authenticate requests made to the Gateway API. This guide offers step-by-step instructions for setting up and managing Private Apps on the Gateway. 

## How to Create a new Private App

_Please note that HDR UK cannot create Private Apps on behalf of users._

### Step 1: Sign into the Gateway

Sign in to the Gateway with your preferred login provider. Make sure you have a ‘team’ set up on the Gateway. If you are not a member of an existing ‘team’ you may need to ask a Team Admin to add you  to the team (see documentation [here](https://www.healthdatagateway.org/about/how-to-manage-teams-on-the-gateway) on how to manage ‘team’ on the Gateway). If you need assistance with this step, contact the HDR UK Technology Team using the link below. 

[https://www.healthdatagateway.org/about/contact-us](https://www.healthdatagateway.org/about/contact-us)


### Step 2: Access the Gateway Private App management page

Providing you have the necessary roles (Team Admin or Developer), you can access the feature by following these steps: 

- Navigate to your Team Management page by clicking on your name in the top-right corner of the window, and selecting the your ’team’ from the dropdown list. 
- In the menu on the left-hand side, select Integrations > Private Apps. 
-   Click on the Create Private App button to initiate the process (Fig 1) 

![](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/4dd0dbc8-10ae-46a0-b567-9c98c3367987)
_Fig 1: How to create a new Private App_

### Step 3: Enter Private App details

To create a new Private App you will need to enter the following information (Fig 2):

- Public App name: Name of the App you wish to create. 
- Description: A brief description of the App. 
- Notification contacts: Gateway user accounts for relevant notification recipients. 

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/5667e21e-576d-4aec-9a96-92448c4375fc)
_Fig 2: App info_


### Step 4: Define permissions

Use the permissions matrix (Fig 3) to assign the appropriate permissions for secure integration. Your App will only be allowed to use APIs for the permissions you have defined. App permissions are the responsibility of your ‘team’.  

If you have any questions about defining Private App permissions, please contact the HDR UK Technology Team using the URL below. 

[https://www.healthdatagateway.org/about/contact-us ](https://www.healthdatagateway.org/about/contact-us)

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/6146a122-e2fb-4daf-a514-f69d2008e178)
_Fig 3: Permissions matrix_

We recommend only assigning permissions that the App will need and suggest a minimal permissions approach, for example: if an App is going to be managing Datasets we would recommend `datasets.create`,  `datasets.read`,  `datasets.update`,  and `datasets.delete`. There would be no need to grant the App permissions to manage Tools or Data Uses in this instance. 

Once the desired permissions are set, click the Save & Finish button to complete the Private App setup. Please note, at the current time, only functionality for Datasets has been enabled on the Gateway.

### Step 5: Authentication Keys

Click on the newly created App entry. The AppID and ClientID will be accessible in the Authentication tab after completing the App setup (Fig 4). Both the AppID and Client ID are crucial as any requests to an authenticated Gateway API endpoint will require these to validate the request. Please see the documentation _link_ which demonstrates how to make an authenticated API request to the Gateway. 

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/2c0ec13f-bbe8-4a07-94ee-adc9b8c5620a)
_Fig 4: Authentication_


## Manage APIs

### List of Private Apps

Via the Private App management page, click on the Manage Private Apps button (Fig 5) to see a list of enabled and disabled Private Apps . 

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/f363f047-6d33-4030-bda1-3fbedd612f7c)
_Fig 5: Manage Private Apps_

Each App is listed with its title, creation date, App ID, and a brief description. The list (Fig 6) can be filtered by App status. 

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/75c7784e-35f4-4a40-b58a-0fb8007c0a0b)
_Fig 6: List of Private Apps_


### Update a Private App 

Select the App you wish to modify, and then update the App information and permissions settings. Click the Save button to store the updated information on the Gateway. A pop-up window will confirm the successful App update . 

The App’s ClientID will not automatically regenerate when permissions or information is changed. If you are making significant changes to the permissions of an App we recommend either disabling or deleting the old Private App and creating a new one. 

Please note that deleting an App is an irreversible action. 