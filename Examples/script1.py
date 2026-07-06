print ("Always executed")

def calculate_sum(a, b):
    if a < 0 :
        return a + b
    else:
        return a + b + 1
 
if __name__ == "__main__":
    print ("Executed when invoked directly")
    print(calculate_sum(2,2))
    print(__name__)
    
else:
    print ("Executed when imported")
    print(calculate_sum(5,5))
    print(__name__)