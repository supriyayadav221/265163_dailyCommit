'''Write a Python program to convert a list of tuples into a dictionary'''

def listtodict(A, di):
   di = dict(A)
   return di

# Driver Code
A = [("Adwaita", 5), ("Aadrika", 5), ("Babai", 37), ("Mona", 7), ("Sanj", 25), ("Sakya", 30)]
di = {}
print ("The Dictionary Is ::>",listtodict(A, di))