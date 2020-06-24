Homeworks for GL QA Automation ProCamp'2020,
Selenium section

For all homeworks:
1. Create virtual environment;
2. Activate the virtual environment;
3. Install all the libraries from the requirements file in the root folder:
pip install -r requirements

For homeworks_1_2:
1. cd into the homeworks_1_2 folder;
2. run pytest with the key -v (more readable output):

(venv) user@user: GL_ProCamp_2020_Selenium/homeworks_1_2$ pytest -v

For homeworks_3:
1. cd into the homework_3 folder;
2. run pytest with keys -v and -s (-s enables stdout capturing for the listener's output,
-v - makes the output more readable):

(venv) user@user: GL_ProCamp_2020_Selenium/homeworks_3$ pytest -vs
