from django.shortcuts import render
import joblib

     
      
def home(request):
  return render(request,"main.html")

def result(request):
  
  cls =joblib.load('job_modell.sav')
  
  lis=[]
  
  lis.append(request.GET['pclass'])
  lis.append(request.GET['sex'])
  lis.append(request.GET['age'])
  lis.append(request.GET['sibsp'])
  lis.append(request.GET['parch'])
  lis.append(request.GET['fare'])
  lis.append(request.GET['embC'])
  print(lis)
  
  ans=cls.predict([lis])

    
    
    

  if ans == 1:
   ans = 'yes'
  elif ans == 0:
   ans = 'no'
  else:
   ans = 'error'  
  return render(request,'result.html',{'ans':ans,'lis':lis})
 
    

   
   
       
    

 
  
  

    
    
  
  
  