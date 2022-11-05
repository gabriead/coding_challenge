# Deepopinion Coding Challenge

## Step 0 - Clone coding challenge Repo
Go to https://github.com/gabriead/coding_challenge and clone the repo locally

## Step 1 -  Start Zammad and login
I assume that you have a local Zammad instance up and running. If not follow the instructions here: 
https://docs.zammad.org/en/latest/install/docker-compose.html;

## Step 2 - Create or add your user token to Zammad
Create a token within Zammad that has sufficient rights
Go to "Profile" -> "Token Access" -> "Create" and add a user with
the permissions  "admin" and  "ticket.agent". Save the token for later use.

## Step 3 - Add token to the application
In order to use Zammad with the user (that has the rights mentioned above) add your token
to "app_config.py" at the marked position. You find the file under the src/ folder.

## Step 4 - Create local environment to install dependencies
Create a local environment where the requirements.txt can be installed and activate it

## Step 5 - run the program
In order to run the program you will have to install the requirements first.
Step 1 : Navigate to the src path where your Github repo lives (e.g. ~/Desktop/coding_challenge/src)
Step 2: type "pip install -r requirements.txt" into the console
Step 3: type "python import_tickets_zammad.py" into the console
Voila you executed the application.

