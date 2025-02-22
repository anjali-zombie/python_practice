questions =[
        [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php",  1
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 2
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php",  4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 2
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 1
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php",  1
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 2
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 2
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 1
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 1
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 2
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php",  4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php",  4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php",  3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 2
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 1
  ],
]

levels = [1000,2000,3000,4000,5000,10000,20000,30000,40000,50000,100000,200000,300000,400000,500000,1000000]
money =0;



for i in range(0,len(questions)):

    question = questions[i]
    print(f"question number {i+1} is for money {levels[i]}") 
    print(f"{question[0]}")
    print(f"a. {question[1]}   b.{question[2]}")
    print(f"c. {question[3]}   d.{question[4]}")

    reply = int(input("enter correct option between 1-4 or 0 to quit: "))
    if(reply == 0):
        money = levels[i-1]
        break;
    if(reply == question[-1]):
        print(f"your answer is correct!!!! you won {levels[i]} Rs")
        if(i == 5):
            money = 10000
        elif(i == 10):
            money = 100000

        elif(i == 15):
            money = 1000000

    else:
        print("wrong answer")
        break

print(f"money you are taking home is {money}")







