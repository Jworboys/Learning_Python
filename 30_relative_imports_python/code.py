''' You cant use relative imports from  
    the file where you run the program'''

import mymodule

print("code.py: ", __name__)