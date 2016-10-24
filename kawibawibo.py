import random

================================================
컴퓨터와 하는 가위 ! 바위 ! 보 !
================================================
관련 작업자
===========
* 정희재 (Jeong hee jae)
* 이원정 (Lee won jeong)

---------------------------------------
작업일지
---------------------------------------
* 2016.10.12 Wednesday

---------------------------------------

def main():
	'''
	컴퓨터와 가위바위보를 하는 프로그램이다.
	사용자가 가위, 바위, 보 중 하나를 입력하기 전에 
	컴퓨터가 가위, 바위, 보 중 무작위로 하나를 선택하고
	입력한 후 누가 이겼는지 결과를 출력해준다.
	'''
	com_finger = random.randrange(3) + 1
#자신이 낼 가위바위보를 선택합니다.
	for i in range(10):
		my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		while not(my_finger == 1 or my_finger == 2 or my_finger ==3):
			my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		
#컴퓨터가 가위를 냈을 경우
		if(com_finger == 1):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은?! 가위입니당. -----> Draw !")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은?! 가위입니당. -----> You win !")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은?! 가위입니당. -----> You lose !")
		
#컴퓨터가 바위를 냈을 경우
		elif(com_finger == 2):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은?! 바위입니당. -----> You lose !")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은?! 바위입니당. -----> Draw !")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은?! 바위입니당. -----> You win !")
		
#컴퓨터가 보를 냈을 경우
		elif(com_finger == 3):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은?! 보입니당. -----> You win !")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은?! 보입니당. -----> You lose !")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은?! 보입니당. -----> Draw !")