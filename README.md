# Instractions for installation of Habit App
First, create a new folder and open it using a prefered text editor such as Visual Studio Code

Then open the git bash and clone the project using the following line of code; git clone https://github.com/filmon-yoha/Habit-App.git

Next open up the terminal and open the virtual environment using the following line of code; python -m venv .\venv

To activate the virtual environment use the following code; venv\scripts\activate

To install the packages required, first call upon the correct file using cd Habit-App and then type the following code; pip install -r requirements.txt

Then execute the written SQL code using the following code; py manage.py makemigrations

Next execute the default SQL code using the code; py manage.py migrate

Then run the server using; py manage.py runserver

After the execution of the code,click on the link that appears which will directly lead to the app

to run the tests use the code; py manage.py test
