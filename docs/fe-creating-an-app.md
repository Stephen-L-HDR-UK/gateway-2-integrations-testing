## Introduction

The API Management Service enables data custodians to streamline metadata transfer to the Gateway
through the creation of API keys. This guide offers step-by-step instructions for setting up and managing the
API self-service on the Gateway.

## Create a new API key

The API management feature allows data custodians to create API keys and ?link them to the Gateway.
Please note that HDR UK cannot create application registrations on behalf of users.

### Step 1: Sign into the Gateway

Sign in to the Gateway with your preferred route. Make sure you have a Team set up on the Gateway. If
you need assistance with this step, contact the HDR UK technology team using the link below.

[https://www.healthdatagateway.org/about/contact-us](https://www.healthdatagateway.org/about/contact-us)

### Step 2: Access the Gateway API management page

If you have the necessary permissions (Team admin or Developer), you can access the service by following
these steps:

-   Navigate to the Team Management page for your Team, by clicking on your name in the top-right corner of the window, and selecting the appropriate Team name in the dropdown list.
-   In the menu on the left-hand side, select `Integrations > API management`.
-   Click on “Create API-key” to initiate the process (Fig 1)

![](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/4dd0dbc8-10ae-46a0-b567-9c98c3367987)
_Fig 1: Create a new API key_

### Step 3: Create a new API Key

When creating a new API Key, provide the following information (Fig 2):

- Public app name: Name of the app you wish to create.
- Description: A brief description of the app.
- Notification contacts: User accounts for relevant notification recipients.
- After completing the required fields, click "Save & Continue" to proceed to the permissions page.

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/5667e21e-576d-4aec-9a96-92448c4375fc)
_Fig 2: App info_

### Step 4: Define Permissions

Use the permissions matrix (Fig 3) to assign the appropriate scope and permissions for secure integration.
Your application will only synchronise data within its assigned scope. Application permissions are the
responsibility of your publisher team.

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/6146a122-e2fb-4daf-a514-f69d2008e178)
_Fig 3: Permissions matrix_

It is recommended that when creating Apps on the Gateway you only assign permissions that the app will
need. We would suggest a minimal permissions approach, for instance: if an App is going to be managing
Datasets we would recommend `datasets.create`, `datasets.read`, `datasets.update` and `datasets.delete`. There
would be no need to grant the app permissions to manage Tools or Data Uses.

Once the desired permissions scope is set, click "Save & Finish" to complete the API setup. Please note, at
the current time, only functionality for Datasets has been enabled on the Gateway.

Click on the newly-created app\s entry. The API key will be revealed in the "Authentication" tab after completing the app setup (Fig 4). The Client ID is
crucial for configuring your API settings; ensure to copy it and apply it to your API settings accordingly.

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/2c0ec13f-bbe8-4a07-94ee-adc9b8c5620a)
_Fig 4: Authentication_

## Manage APIs

### List of APIs

Clicking on “Manage API” (Fig 5) displays a list of enabled and disabled APIs for easy management and
monitoring of apps.

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/f363f047-6d33-4030-bda1-3fbedd612f7c)
_Fig 5: Manage API_

Each app is listed with its title, creation date, APP ID, and a brief description. The list (Fig 6) can be filtered
by App status.

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/75c7784e-35f4-4a40-b58a-0fb8007c0a0b)
_Fig 6: List of Apps_

### Modifying an API

Select the app you wish to modify, and you can update the app information and permissions settings.
It's important to note that deleting an API is an irreversible action.

### After updating the app:

Once you've updated the app, click "Save" to store the updated information on the Gateway. A pop-up
window will confirm the successful application update. Additionally, a new Client ID will be generated in the
Authentication tab, which you need to copy and replace in your API settings. This final step ensures
seamless integration and efficient data synchronisation.

![image](https://github.com/HDRUK/gateway-2-integrations-testing/assets/69473770/ec7175a0-1871-42a2-8450-466d6503b13b)
_Fig 7_

### Caveat

It is important to note that there are several methods of managing metadata on the Gateway. In the
instance where metadata is onboarded onto the gateway though Entity Federation (FMA), these datasets
will not be editable via the User Interface, OR via the API and will result in a 403 forbidden response being
returned. In cases where a Data Partner wants to manage data via API and Federation, federated items will
not be editable via API.
