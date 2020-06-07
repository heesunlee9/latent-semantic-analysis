# Latent Semantic Analysis(LSA)
Last Update: 2020/06/08

<img src=/lsa_overview.png height="700"></img>

# Feature
When you enter your documents and topic names, LSA offers a topic name that each document is most related. <br>

e.g. document: I like studying the greenhouse effect. <br>
     topic names: environment, cuisine, sports...<br>
     result: environment<br>
     
문서와 토픽 이름 입력시 개별문서와 매칭되는 토픽 이름이 매칭 됩니다. 

# Latent Semantic Analysis was developed using 
flask, numpy, sklearn, python, latent semantic analysis <br>

# Latent Semantic Analysis was developed by 
heesunlee9 in December 2019.

# How to Start
1. pip install virtualenv

2. virtualenv [your virtual environment name] <br>
e.g. virtualenv venv

3. source [your virtual environment name]/bin/activate <br>
(on Windows: [your virtual environment name]/bin/activate.bat)

4. pip install flask <br>
pip install sklearn <br>
pip install numpy

5. python3 app.py <br>
click 'http://127.0.0.1:5000/' with ctrl-key
