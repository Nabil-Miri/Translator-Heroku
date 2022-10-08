# Eng_Fr_Translator
English to French Translator model Deployment using Flask, Docker and Heroku

We have did the following few steps to reach the final deployment app :
## 1: Downloading the final model
we rerun our project again and we have downloaded the final model to get ready to make it as app and deploy it 
## 2: Creating HTML page
we have created a HTML page to let the user deal with our model so we have prepared the page
## 3: Using Flask as framework
We created app.py which is contains the flask code and it imports the EnFrTranslator class from model.py file.
so we connect the HTML page to the Flask framework to let the user interact with the box and the button, so now users can write an english sentence in a textbox and click the tranlate button to let the model predict it and translate the sentence to french
## 4: Deploying model using Heroku (No Docker)
There are 2 ways:
1) connect directly the github repo to heroku using the website
2) Downloading Heroku CLI and using it to deploy the model
We first tried to connect to the github repo and it worked but we had some errors whe deploying which couldnt be visualized this way. Thus, we used Heroku CLI and runned the commands using git bash. We used 'heroku logs --tail' to know what were the errors and we faced sever ones such as:
A. The file structure was not right and we fixed it.
The structure should be:
![image](https://user-images.githubusercontent.com/75530842/194516888-235c3f91-201d-4993-b224-15e5a71ee705.png)
- runtime.txt: Used by Heroku to know which python version we want it to use and the list of supported versions are found on the website.
![image](https://user-images.githubusercontent.com/75530842/194517148-0c4c57c8-3dca-4662-a871-a7effaa9afed.png)
- requirments.txt: Used by Heroku to know the needed libraries and their versions (also needed by Heroku)
![image](https://user-images.githubusercontent.com/75530842/194517474-6d59c34a-1cd6-43a9-8416-080170107910.png)
- app.py: our main code. it should be in the main root of the file so that heroku could detect that it is a python build (it can detect this also from the requirments,txt)
- Procfile: a file without extension for heroku to know the main file
![image](https://user-images.githubusercontent.com/75530842/194517915-834bf512-e745-462a-8c6f-24a5ef7919e5.png)
Note: if your main py file is not named as app, you could change it in the procfile also.

B. Size of the Heroku Slug is > 500 MB
This happened when 'tensorflow' was in the requirments as it is around 450MB and something more. After a lot of testing we found 'tensorflow-cpu' a much smaller version which solved the problem.

When we do any change in the repo we do 'git push heroku main' and after it finishs, we type 'heroku open' which will open the link in the browser

## 5: Deploying model using Heroku (Docker)

# Creating Docker Container
we then get prepare the containers with all the required dependencies to move it into cloud using Docker, so users can deal with the app without risks and problems
First we login to docker 
docker login
then we prepare the Dockerfile:

![image](https://user-images.githubusercontent.com/75530842/194549461-19f449df-841c-43b1-a388-b71119b53a43.png)

We build an image either using the docker plugin in pycharm which is connected to Docker Desktop or by using the docker command in the git bash. The command for building a docker image is:  docker build -t heroku-translator-cmd -f Dockerfile .

![image](https://user-images.githubusercontent.com/75530842/194709746-a7615080-ee00-488b-af26-9c7b6fd7694a.png)

![image](https://user-images.githubusercontent.com/75530842/194709756-1d39d1d8-78ac-4687-ad05-88f78b483c03.png)

![image](https://user-images.githubusercontent.com/75530842/194709775-d3faf236-8bf0-4cf4-85b3-d8f133afd658.png)

![image](https://user-images.githubusercontent.com/75530842/194710296-6fd951c2-b84e-4d57-ba0a-bdc98845b7da.png)

![image](https://user-images.githubusercontent.com/75530842/194710406-26a990fa-b3f3-404b-8bce-b0cf68c7daa8.png)




## Finally : Heroku cloud
sure we have committed and pushed all the files that we used for deployment into a github repository, so now we can easily access it from Heroku cloud to deploy the created app 
