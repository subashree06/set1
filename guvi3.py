def reverse(string): 
    string = string[::-1] 
    return string 
  
s = "aabbcc"
  
print ("The original string  is : ") 
print (s) 
  
print ("The reversed string(using extended slice syntax) is : ") 
print (reverse(s))
