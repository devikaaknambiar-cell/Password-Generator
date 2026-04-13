# Password-Generator
A python password generator that creates secure random passwords using 'secrets'

The program enables users to customise the password length and choose whether to include uppercase letters, numbers and symbols. The main logic works by creating a pool of characterss, then randomly selecting characters from that pool to create a password of the desired length. 

FEATURES:
1. Generates secure random passwords
2. Customizable password length (1-16)
3. Options include;
   - uppercase letters
   - numbers
   - special symbols
4. Use's 'python secrets'  moduel for secure randomness

TECHNOLOGY USED:
1. IDLE python 3.13
2. Built in python libraries
   - secrets
   - string
  
HOW IT WORKS:
The program asks the user for:
1. Desired password length
2. Whether uppercase should be included
3. Whether numbers should be included
4. Whether symbols should be included
It then builds a character set based on the users personal choices and randomly selects characters to create the new password

EXAMPLE OUTPUT:
Password length (defult 16): 8
Include uppercase? (Y/N): Y
Include numbers? (Y/N): y
Include symbols? (Y/N): n

Your password: TBkRTzoJ


