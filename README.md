# astrology-app

## installation
- pip install Pillow
- cd Morinus/SWEP/src/; python setup.py build install
  - on windows, download and install minGW
  - python setup.py build install --compiler=mingw32
  - must add bin file inside mingw to path

## run
python Morinus/morinus.py

todo:
- table
- houses
- chart (as png)
- aspects (for now, as png)

1. new branch for issue
2. code! 
3. pull request 
4. after code review, merge
5. delet branch and repeat 

##Future Features
 - ability to process a refund for a person in the admin panel
 - ability to send email to all customers at once
 - ability to delete a customer from the database 
 - ability to see total number of pending customers
 - any other customer analytics 
 - searchable list of all customers by email

##Setup help:
    - google analytics
    - paypal
    - mongo hosting
    - heroku
    - 
```
zodiacs:
ARIES = 0
TAURUS = 1
GEMINI = 2
CANCER = 3
LEO = 4
VIRGO = 5
LIBRA = 6
SCORPIO = 7
SAGITTARIUS = 8
CAPRICORNUS = 9
AQUARIUS = 10
PISCES = 11

planets:etc

A SUN
B MOON
C MERCURY
D VENUS
E MARS
F JUPITER
G SATERN
H URANUS
I NEPTUNE
J PLUTO
K 
L

these are symbols in planatary aspects
S - trianlge
R - square
P - astrics
W - the 0-0 looking one(its slanted)
```