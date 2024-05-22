def grade(score):
    score=''
    #print('Your score is ')
    
    if score <=20 and score <=50:
        print('You need to work hard')
    elif score >50 and score <=70:
        print('You need to study. above average')
    elif score >70 and score <=90:
        print('Good work. Keep it up')
    else:
        print('Excellent work. Keep it')
  
mark=int(input('Enter your marks'))
res=grade(mark)        
# mark=grade(score)
print(res)
       