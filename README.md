# RASA basic math bot ( With Whatsapp deployment)

# Project Objective:
•	Build a Bot to do basic mathematical operations
•	Proposed workflow for the Bot
   1. Take two operands and operation as input and show the output
   2. Show the available mathematical operations
      •You can use a simple menu based approach to take the operation
      •Example categories: “addition”, subtraction”, ”multiplication”, “division”
   3. Based on these input show the output for the users
   4. After the flow ends - If a user says ”more operations” , take       the new inputs and proceed
      •For example (let us say user asked for sum of 4 and 5)


# Steps to implement rasa:
 
1.	Create a virtual environment and install rasa from conda in python.
2.	Train the basic model and run it.
3.	You can train the model by using a command,
rasa train
4.	You can run the bot in shell by command,
rasa shell or rasa run

# Steps to create the required bot:

# Edit the following files:

5.	domain.yml: This file defines the domain of the chatbot, including the intents, entities, slots, and actions. It serves as a central place to define all the objects and their properties that the chatbot will use. It also defines the responses that the chatbot can provide to the user.
6.	nlu.yml: This file contains the training data for the natural language understanding (NLU) module of the chatbot. It includes examples of user input and the corresponding intent and entity labels. The NLU module uses this file to learn how to map natural language user inputs to the appropriate intents and entities.
7.	stories.yml: This file contains stories or dialogues that describe the interactions between the user and the chatbot. Each story is a sequence of user inputs and the corresponding bot responses. These stories serve as training data for the dialogue management module of the chatbot.
8.	rules.yml: This file contains rules that describe specific conditions that trigger certain bot actions. Unlike stories, rules are written in a more declarative format and can help the chatbot handle specific situations more efficiently.
9.	actions.py: This file contains the code that defines the custom actions that the chatbot can take. These actions can be anything from sending an email or querying a database to providing a recommendation or asking for more information. The actions defined in this file can be called from the dialogue management module in response to user inputs.



# Train the model :
Your Rasa model is trained and saved at 'models\20230228-130421-immense-radon.tar.gz'.

# Run your rasa model(rasa run):

Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  hi                                      
Hey! How are you?I can help you perform basic mathematical operations. What would you like me to do?
Your input ->  can you do a math operation             
What type of mathematical operation do you want to perform?
Your input ->  addition                                
What is the first number?
What is the second number?
Your input ->  5 2                                     
The result of addition of 5.0 and 2.0 is 7.0.
Thank You!
Your input ->  perform another operation               
What type of mathematical operation do you want to perform?
Your input ->  subtraction                             
What is the first number?
What is the second number?
Your input ->  8 2                                     
The result of subtraction of 8.0 and 2.0 is 6.0.       
Thank You!
Your input ->  perform another operation               
What type of mathematical operation do you want to perform?
Your input ->  division                                
What is the first number?
What is the second number?
Your input ->  5 0                                     
The second number cannot be 0. Please enter a valid number.                              
Your input ->  goodbye                                 
Bye
Your input ->  /stop    




# Screenshots:


# (1) Project Folder:
![image](https://user-images.githubusercontent.com/81423983/221855375-d3dfea60-e00c-45a9-8033-57cbf1177537.png)


# (2) Hosting the bot model using ngrok:
![image](https://user-images.githubusercontent.com/81423983/221855551-c4d8a8e2-d255-4ef8-a7c2-e77201fa8f42.png)

# (3) Ngrok status panel:
![image](https://user-images.githubusercontent.com/81423983/221855890-6ecb3fb7-c6f0-41cf-a5d2-5db02269e9d1.png)

 

# Deployment in whatsapp using twilio.com:
 

# (4) Using whatsapp sandbox of twilio.com in whatsapp:
![image](https://user-images.githubusercontent.com/81423983/221856051-73757c68-72cc-44df-8c5b-1bf4e00a62b5.png)

# (5) Whatsapp web Chat with bot :
![image](https://user-images.githubusercontent.com/81423983/221856242-c5c7bfa9-ec2e-4f24-b645-b8f2c9dc4445.png)

![image](https://user-images.githubusercontent.com/81423983/221856283-62367d75-defe-4fde-956a-75ca865b3d57.png)


# (6) Whatsapp app Chat with bot in mobile:
![image](https://user-images.githubusercontent.com/81423983/221856484-c464932d-9115-40a1-8377-a00b130105f4.png)

![image](https://user-images.githubusercontent.com/81423983/221856567-96100fdb-bf0e-4f82-8a86-3611830e74a8.png)

# (7) Code Editor:
![image](https://user-images.githubusercontent.com/81423983/221856747-073a9788-9813-48bb-a914-54a806e3a6d0.png)

![image](https://user-images.githubusercontent.com/81423983/221856780-096633e2-3835-4bd1-a8a6-18b25646f90e.png)

![image](https://user-images.githubusercontent.com/81423983/221856828-1246bf06-c045-4207-9c76-7ec16ca78c32.png)


# Commands Used:

1. For Training model:
   rasa train

2. For shell chat with bot:
   rasa run actions
   rasa shell

3. Making bot available to ngrok:
   rasa run -m models --enable-api --cors "*"

4. Making ngrok to make our bot global:
   ngrok.exe http 5005

5. Whatsapp number of chatbot deployed:
   +1 (415) 523-8886
   
   to start the bot:
   join interest-law
   
   hi (or any other greet)
   
   to stop the bot:
   stop
   
 

              






 





          
