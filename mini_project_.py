import pickle  # imported module to handle binary file operations
print(" ........ A STUDENT DATA BASE MANAGEMENT SYSTEM.......")
print("    MENU -  Choose An Action You want To Perform : ")
print("      1.  CREATE FRESH DATABASE - ENTRY SESSION ")
print("      2.  DISPLAY RECORDS OF  ALL STUDENTS ")
print("      3.  SEARCH AND DISPLAY RECORD OF A STUDENT USING ROLL NO  ")
print("      4.  INSERT A NEW STUDENT RECORD AT A SPECIFIED LOCATION ")
print("      5.  DELETE A STUDENT RECORD BASED ON ROLL NO")
print("      6.  UPDATE MARKS OF  A STUDENT ")
print("      0.  EXIT AND STOP ")

while True :  # outermost block - FOREVER LOOP-- INFINITE LOOP
 choice=int(input("Enter Choice(1-Create 2-Disp 3-Search 4-Insert 5-Del 6-Update 0-Exit ): "))

 if choice==1 :  #CREATE FRESH DATABASE - ENTRY SESSION
  n= int(input('Enter number of students :'))      
  f = open('mybinary.dat','wb')
  
  for i in range (1,n+1):
    print("\n Enter data of a students Serial Order Number :",i)
    rollno = int(input('Enter roll number:'))
    name = input('Enter Name:')
    Class = input('Enter Class :')
    marks = float(input('Enter Marks'))
    #Creating the dictionary
    rec = {'Rollno':rollno,'Name':name,'Class':Class,'Marks':marks}
    #Writing the Dictionary
    pickle.dump(rec,f)
  f.close()
	
 elif choice==2 : #DISPLAY RECORDS OF  ALL STUDENTS 
 
  f= open("mybinary.dat", "rb")
  while True:
   try:
    r=pickle.load(f)
    print(r)
   except EOFError:
       break
  f.close()
	
 elif choice==3 :  # SEARCH AND DISPLAY RECORD OF A STUDENT USING ROLL NO

  f = open('mybinary.dat','rb')
  flag = False
  r=int(input( "Enter roll no of a student  to be searched "))
  while True:
   try:
     rec = pickle.load(f)
     if rec['Rollno'] == r:
         print('Roll Num:',rec['Rollno'])
         print('Name:',rec['Name'])
         print('Marks:',rec['Marks'])
         flag = True
   except EOFError:
         break
  if flag == False:
     print('No Records found')
  f.close()
	
 elif choice==4 :  # insert a new record at a specified position

   f = open('mybinary.dat','rb')
   reclst = []
   position=int(input( " Enter the position at which you want to insert (position <n)"))
   print("\n Enter data of  a student to be inserted  :")
   rollno = int(input('Enter roll number:'))
   name = input('Enter Name:')
   Class = input('Enter Class :')
   marks = float(input('Enter Marks'))
   #Creating the dictionary
   record = {'Rollno':rollno,'Name':name,'Class':Class,'Marks':marks}
   #Writing the Dictionary
   while True:    
     try:
      rec = pickle.load(f)
      reclst.append(rec)
     except EOFError:
           break
   f.close()
   reclst.insert(position-1,record)
   f = open('mybinary.dat','wb')
   for x in reclst:
     pickle.dump(x,f)
   f.close()

 elif choice==5 :  # delete a record of student with given roll no
     f = open('mybinary.dat','rb')
     reclst = []
     r=int(input("enter roll no to be deleted"))
     while True:
       try:
        rec = pickle.load(f)
        reclst.append(rec)
       except EOFError:
             break
     f.close()
 
     f = open('mybinary.dat','wb')
     for x in reclst:
        if x['Rollno']==r:        
           continue
        pickle.dump(x,f)  # dead code
     f.close()

 elif choice==6 :  #UPDATE MARKS OF  A STUDENT
     f = open('mybinary.dat','rb')
     reclst = []
     r=int(input("enter roll no to be updated"))
     m=float(input(" enter correct marks"))
     while True:
      try:
        rec = pickle.load(f)
        reclst.append(rec)
      except EOFError:
             break
     f.close()
     for i in range (len(reclst)):
      if reclst[i]['Rollno']==r:
       reclst[i]['Marks'] = m
       f = open('mybinary.dat','wb')
     for x in reclst:
        pickle.dump(x,f)
     f.close()

 elif choice==0 :  # STOP  -  EXIT-- GOOD BYE-- END OF WHILE LOOP
         print("\n Good Bye... Have a nice Day ")
         print("   This is positively not an end...It is a New Beginning !!")
         break   # Terminate forever while loop
  
 else :
    print("Invalid Choice....Try Again")
