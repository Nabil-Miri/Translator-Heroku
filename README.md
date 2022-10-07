# Eng_Fr_Translator
English to French Translator model Deployment using Flask, Docker and Heroku

We have did the following few steps to reach the final deployment app :
## 1: Downloading the final model
we rerun our project again and we have downloaded the final model to get ready to make it as app and deploy it 
## 2: Creating HTML page
we have created a HTML page to let the user deal with our model so we have prepared the page
## 3: Using Flask as framework
so we connect the HTML page to the Flask framework to let the user interact with the box and the button, so now users can write an english sentence in a textbox and click the tranlate button to let the model predict it and translate the sentence to french
# Deploying model using Heroku (No Docker)
There are 2 ways:
1) connect directly the github repo to heroku using the website
2) Downloading Heroku CLI and using it to deploy the model
We first tried to connect to the github repo and it worked but we had some errors whe deploying which couldnt be visualized this way. Thus, we used Heroku CLI and runned the commands using git bash. We used 'heroku logs --tail' to know what were the errors and we faced sever ones such as:
1. The file structure was not right and we fixed it.
The structure should be:
![image](https://user-images.githubusercontent.com/75530842/194516888-235c3f91-201d-4993-b224-15e5a71ee705.png)



First thing is to downoad Heroku CLI
## 4: Dockerization
we then get prepare the containers with all the required dependencies to move it into cloud using Docker, so users can deal with the app without risks and problems

## Finally : Heroku cloud
sure we have committed and pushed all the files that we used for deployment into a github repository, so now we can easily access it from Heroku cloud to deploy the created app 
