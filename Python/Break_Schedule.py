#importing the time module
import time

#importing the web browser module
import webbrowser

#defining functions to open a particulqar browser on specific breaks

#defining music function which opens music page on web browser
def music():
  webbrowser.open('https://www.youtube.com/', new=2)

#defining snacktime function which opens food blog on web browser
def snacktime():
  webbrowser.open('https://detailed.com/food-blogs/', new=2)

#defining dance function which opens dance blog on web browser
def dance():
  webbrowser.open('http://www.arthurchandler.com/dance', new=2)

#initializing count=0 to count the number of breaks taken
count=0

#calling sleep method to open the web browser in 2 seconds
def sleep():
  time.sleep(2)
  

#loop to iterate until the condition is true
while True:
      print("Enter \n  5)for music \n 6)for snacktime \n 7)for dance \n 8)exit")
      inp=int(input("Enter input"))
      if inp==5:
          sleep()
          music()
          count=count+1
      elif inp==6:
          sleep()
          snacktime()
          count=count+1
          
      elif inp==7:
          sleep()
          dance()
          count=count+1
      elif inp==8:
          break
      else:
          print("invalid input")


#print the count value that is the number of breaks taken 
print("no of time taken break",count)

  
  
    





