import threading,requests #Import all required modules
url = input("URL to ping: ") #Ask for the URL to send requests to
if url.startswith('http://'): #See if URL starts with valid protocol
     pass #Passing since valid protocol
elif url.startswith('https://'): #Looping the valid protocol check
     pass #Passing again since valid protocol
else: #If not valid protocol
     url = "http://" + url #Adding the http:// protocol
times = int(input("How many times do you want to ping that website?: ")) #Asking how many requests should be sent to website
print("Attempting to start sending requests...") #Takes a while so cool message
def send_request(): #Sending request function
     response = requests.get(url) #Sending request
     if response.status_code != 200: #Checking if not code 200
          print("Status code: " + str(response.status_code) + " | Request has not reached destination") #Sending status code
     else: #Else (status code 200)
          print("Status code: " + str(response.status_code)) #Notify user of successful request
Threads = [] #Adding threads to join
for _ in range(times): #Looping over the "times" variable
     startThread = threading.Thread(target=send_request) #Making new thread
     startThread.start() #Starting new thread
     Threads.append(startThread) #Appending the thread to the "Threads" list
for Thread in Threads: #For every object (thread) in Threads (list of threads)
     Thread.join() #Join the thread
input("PRESS ENTER TO CLOSE >>> ") #So the Python window does not automatically close and user knows their task has finished