import random
import time
from datetime import datetime





desert_dic = {'초코케이크' : 3000,'딸기케이크' : 3500, '당근케이크' : 4000}
beverage_dic = {'초코라떼' : 1500,'딸기라떼' : 2500, '아메리카노' : 1000}


print("디저트 카페에 오신 것을 환영합니다.")
print("주문을 종료하고 싶으면 q를 입력해주세요.\n")
print("=====메뉴판======")

print("디저트 : ", end="")
print(desert_dic)
print("음료 : ", end="")
print(beverage_dic)

myDesert = []
myBeverage = []

while True:
    desert = input("장바구니에 담고 싶은 디저트를 하나 입력해주세요 : ")
    if desert == "q":
        break
    else:
        print(desert+"가 장바구니에 담겼습니다.\n")
        myDesert.append(desert)

    beverage = input("장바구니에 담고 싶은 음료를 하나 입력해주세요 : ")
    if beverage == "q":
        break
    else:
        print(beverage+"가 장바구니에 담겼습니다.\n")
        myBeverage.append(beverage)

print('\n')
print("장바구니에 담긴 디저트 목록입니다.")
print(myDesert)
print('\n')
print("장바구니에 담긴 음료 목록입니다.")
print(myBeverage)

#디저트와 음료set 각각 생성
myDesertSet=set(myDesert)
myBeverageSet=set(myBeverage)

while True:
    deleteMenu = input("장바구니에서 삭제하고 싶은 메뉴를 하나 입력해주세요 : ")
    if deleteMenu=="q":
        print("최종 장바구니 현황입니다.")
        print(myDesertSet,myBeverageSet)
        print('\n')
        break
    else:
        if deleteMenu in myDesertSet:
            myDesertSet = myDesertSet - set([deleteMenu])
        else:
            myBeverageSet=myBeverageSet-set([deleteMenu])
        print("현재 장바구니 현황입니다.")
        print(myDesertSet,myBeverageSet)
        print('\n')


print("=========== 영수증 ==============\n")


current_time = datetime.now()
print("주문 시간 : ", end="")
print(current_time)

final_myMenu = myDesertSet | myBeverageSet
print("주문 내역 : ", end="")
print(final_myMenu)
print('\n')

price=0

for i in final_myMenu:
    if i in desert_dic:
        price+=desert_dic[i]
    else:
        price+=beverage_dic[i]



print("주문하신 메뉴의 총 금액은 ", end="")
print(price,end="")
print("원입니다.")

print("이용해주셔서 감사합니다.")