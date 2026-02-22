def check_for_word():
  with open("practice.txt","r") as f:
    data = f.read()
    word= "Learning"
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")



def check_for_lines():
     word = "Learning"
     data=True
     line_no = 1
     with open("practice.txt","r") as f:
         while data:
             data = f.readline()
             if(word in data):
                 print(line_no)
             line_no+=1
check_for_lines()