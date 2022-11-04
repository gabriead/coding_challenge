# Deepopinion Coding Challenge

## Step 1 -  Start Zammad and login
I assume that you have a local Zammad instance up and running. If not follow the instructions here: 
https://docs.zammad.org/en/latest/install/docker-compose.html;

## Step 2 - Create or add your user token to Zammad
Create a token within Zammad that has sufficient rights
Go to "Profile" -> "Token Access" -> "Create" and add a user with
the permissions  "admin" and  "ticket.agent"

## Step 3 - Add token to the application
In order to use Zammad with the user (that has the rights mentioned above) add your token code
to "app_config.py" at the marked position

## Step 4 - run the program
In order to run the program you will have to install the requirements first.
Step 1 : Naviagte to the path where your github repo lives (e.g. (base) t2ea@razor-4:~/Desktop/coding_challenge)
Step 2: type "pip install -r requirements.txt" into the console
Step 3: type "python import_tickets_zammad.py" into the console

