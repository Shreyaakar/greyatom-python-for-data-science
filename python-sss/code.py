# --------------
#Code starts here

#Function to read file
def read_file(path):
    file = open(path, 'r')
    scentence = file.readline()
    file.close()
    return scentence 

path = file_path
sample_message = read_file(path)
print(sample_message)  

message_1 = read_file(file_path_1)
print (message_1)
message_2 = read_file(file_path_2)
print (message_2)

def fuse_msg(message_a, message_b):
    v = int(message_a)
    m = int(message_b)
    quotient = m//v 
    str(quotient)
    return quotient


secret_msg_1 = fuse_msg(message_1, message_2)
print(secret_msg_1)

p = read_file(file_path_3)
message_3 = p 
print(message_3)

def substitute_msg(message_c):
    if message_c == "red":
        sub = "Army General"
    elif message_c == "Green":
        sub = "Data Scientist"
    elif message_c == "Blue":
        sub = "Marine Biologist"
    return sub 

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)

message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [x for x in a_list if x not in b_list]
    final_msg = " ".join(c_list)
    return final_msg 

secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3)

message_6 = read_file(file_path_6)
print(message_6) 

def extract_msg(message_f):
    a_list = message_f.split()
    even_word= lambda x: len(x)%2 == 0
    b_list = filter(even_word, a_list)
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)

message_parts=[secret_msg_3, str(secret_msg_1), secret_msg_4, secret_msg_2]   

final_path= user_data_dir + '/secret_mesasge.txt'

secret_msg = " ".join(message_parts)

def write_file(secret_msg, path):
     s = open(path,'a+')
     s.write(secret_msg)
     s.close()

write_file(secret_msg, final_path)
print(secret_msg)
    #Closing of the file
    
    #Returning the first line of the file
    
    

#Calling the function to read file

#Printing the line of the file


#Function to fuse message

    
    #Integer division of two numbers
    
    #Returning the quotient in string format
    
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 



#Function to substitute the messag
    
    #If-else to compare the contents of the file
    
    
    #Returning the substitute of the message
    
    

#Calling the function to read file


#Calling the function 'substitute_msg'


#Printing the secret message



#Function to comp
    
    #Splitting the message into a list
    
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter messag
    
    #Splitting the message into a list

    
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret 




#Combine the secret message parts into a single complete secret message


#Function to write inside
       
    #Opening a file named 'secret_message' in 'write' mode


    #Writing to the file


    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


