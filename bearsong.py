word = "bottles"
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall") # 맥주의 수와 '맥주병' 그리고 나머지 글자를 표시
    print(beer_num, word, "of beer.")
    print("Take one down")
    print("Pass it around") #
    if beer_num == 1: # 만약 맥수의 수가 1과 동일 하다면
        print("No more bottles of beer on the wall.") #더이상 맥주가 있지 않다 라고 표현해라
    else: # 만약 맥주의 수가 1이 아니라면 
        new_num = beer_num - 1 # 새로운 숫자 는 맥주의 수 빼기 1 로 하고 
        if new_num == 1: # 새로운 숫자가 1이 되면
            word = "bottle" # 병 이라는 글자와
        print(new_num, word, "of beer on the wall") # 새로운 수와 '맥주병' 그리고 나머지 글자를 표시 하고
    print() # 이것들을 표현 하려라 .


range(5)
list(range(5))
list(range(5,10))
list(range(0,10,2))
list(range(10,0,-2))
list(range(10,0,2))
list(range(99,0,-1))