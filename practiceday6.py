# day 6 of git practice 
# Today we would be practicing git branching by creating a branch (git branch Day5) Then switch to branch from main by ( git checkout Day5).
# Now create a program here and push to the branch and would merge after 2 days. Until then day 6 and day 7 code will be pushed on the day5 branch created.

# Now day 5 code understanding methods as an OOP study
class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def get_avg(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("Hi!!",self.name,"Your average score is:",(sum//3))

s1=Student("Tony Stark",(99,98,90))
s1.get_avg()

s1.name="Aditya Pandey"
s1.marks=(99,97,98)
s1.get_avg()  
              
# pushed on the Day5 branch and due to (git restore) I lost this comment thus again writing.Now two days only push to this branch and third day would merge in the main. Also to check the current branch name we use (git branch --show-current).                 # day 6 of git practice 
# Today we would be practicing git branching by creating a branch (git branch Day5) Then switch to branch from main by ( git checkout Day5).
# Now create a program here and push to the branch and would merge after 2 days. Until then day 6 and day 7 code will be pushed on the day5 branch created.

# Now day 5 code understanding methods as an OOP study
class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def get_avg(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("Hi!!",self.name,"Your average score is:",(sum//3))

s1=Student("Tony Stark",(99,98,90))
s1.get_avg()

s1.name="Aditya Pandey"
s1.marks=(99,97,98)
s1.get_avg()  

# Now pushed on Day5 branch succesfully , if we want to know the current branch we could use (git branch --show-current) command.                 