
from __future__ import print_function

import random

dictionary = {'집밖에 나가는 것 자체가 스케줄? ':'','불금에는 북적대는 곳보단 집이지? ':'','휴대폰만 있어도 안 심심한가요? ':'','카톡, 문자 알림을 잘 확인하지 않나요? ':'','아무 생각이 없다. 왜냐하면 아무 생각이 없기 때문이다 라고 자주 느끼나요? ':'','당신은 배달앱 VIP인가요? ':'','친구와의 약속이 갑작스레 파토났을 때 아쉽다는 생각보다 오예!라는 생각이 더 자주 드나요? ':''}
question_list=list(dictionary.keys())



def qna(name):
    count=0
    for i in range(0,num):
        question = random.choice(question_list)
        print(question)
        answer=input("답변 : ")
        dictionary[question]=answer
        if answer =="네":
            count+=1
        question_list.remove(question) 
    percent=(count/num)*100   
    your_type(percent)
          

def your_type(percent):
    if percent>75:
        print("당신은 집순이입니다.")
    elif percent>50:
        print("당신은 집을 좀 더 좋아하는군요.")
    elif percent>25:   
        print("당신은 밖을 좀 더 좋아하는군요.")
    else:
        print("당신은 집순이가 아닙니다.")    



name=input("당신의 이름은? ")
print("======안녕하세요 ", end="")
print(name, end="")
print("님! 당신은 집순이일까요?======")
print("======모든 질문의 대답을 네,아니오로 대답해주세요.======")
num=int(input("받을 질문의 개수를 입력해주세요(최대 7개 가능) : "))

qna(name)