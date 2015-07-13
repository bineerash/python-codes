#--------------------------------------------------------------------------
# PGM1-BinayaRajShrestha.py
# Author: Binaya Raj Shrestha
# A program to display students and grades including average, highest,lowest
# and total number of grades
#--------------------------------------------------------------------------

#---------------------------------------------------
#Function that calculates and returns average grade
def calAvg( studentGrades):
    totalGrade = 0
    avg = 0.00;
    for k,v in studentGrades.items():        
        totalGrade = int(v) + totalGrade
    avg = totalGrade/len(studentGrades)
    return avg
#------------------------------------------------

#-----------------------------------------
# Main part of the program
#-----------------------------------------
file = open("scores.txt","r")
lines = file.readlines()
studentGrades = {}
grades = [];
print('%25s' % "Student Name" + '%10s' %   "Grades")
print("-----------------------------------")
if len(lines) >0:    
    for line in lines:  
       if line.strip(): #check empty line
            data = line.split(' ')
            name = [];
        
            # get full name of student
            for i in range(0,len(data)-1):
                name.append(data[i])
            fullName = ' '.join(name)
            grade = data[-1].strip()
            grades.append(int(grade))
                 
            if fullName not in studentGrades:
                studentGrades[fullName] = grade
                print('%25s' % fullName + '%8s' %grade)
               # print('{0:{5}{2}}'.format(fullName, grade),end=' ')
            
    grades.sort() #sort the grades in ascending order

    average = calAvg(studentGrades)
    print ("------------------------------------ ")
    print ('%25s' %"the average grade : ",'%5s' % "{0:.2f}".format(average))
    print ('%25s' %"the highest grade : ", '%5s' % grades[-1])
    print ('%25s' %"the lowest grade : ", '%5s'% grades[0])
    print ('%25s' %"the total number of grades: ", '%2s' % len(studentGrades))
    print ("------------------------------------ ")
else:
    print('%30s' % "No Records found")
    print("------------------------------------")

    
#---------------------------------------------------------------
# Summary of what I gained 
#---------------------------------------------------------------
# While developing this program, I learned about reading and writing file in python.
# I also learned manipulating lines read from a file. Besides file operations, I came
# learned about the for loop and if conditional statement in python which are pretty different
# than in C/C++ in terms of syntax. However, symantically, they behave similar.
# I came across on how a function can be defined and called in python. I also found working in
# List pretty simple and I learned to use dict data type too.
#----------------------------------------------------------------



    
    
    
