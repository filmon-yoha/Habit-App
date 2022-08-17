# Instractions for installation of Habit App
First, create a new folder and open it using a prefered text editor such as Visual Studio Code.
Then open the git bash and clone the project using the following line of code; #git clone https://github.com/filmon-yoha/Habit-App.git.
Next open up the terminal again and open up the virtual environment using the following line of code; python -m venv .\venv
To activate the virtual environment use the following code; venv\scripts\activate
To install the packages required, first call upon the correct file using cd Habit-App and then type the following code; pip install -r requirements.txt
Then run the server using the code; py manage.py runserver
Press the link that appears after the execution of the code which will directly lead to the app
To run the unittests use the code; py manage.py test
