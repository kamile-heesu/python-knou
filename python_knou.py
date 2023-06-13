khan_fp = open('Khan.txt', 'r')
print(khan_fp.read(10))
print(khan_fp.readline())

khan_fp.close()


# ---------------------------

khan_fp2 = open("Khan.txt", "r");

for motto in khan_fp2.readlines():
  print(motto.strip());

khan_fp2.close();


# ---------------------------


h_fp = open("Hamlet_by_Shakespeare.txt", "r");

word_dict = dict();

for line in h_fp.readlines():
  for word in line.strip().split():
    word = word.strip(" .,;?[]\"|':-").lower();

    if word_dict.get(word) is not None:
      count = word_dict[word]
    else:
      count = 0;
    word_dict[word] = count + 1;

for key in word_dict:
  if word_dict[key] > 400 :
    print("{" + key +"}", str(word_dict[key]) + "회")  
  

h_fp.close();

# ---------------------------

import math;

class Cone: 
  def __init__(self, radius = 20, height = 30):
    self.radius = radius;
    self.height = height;
  def get_vol(self):
    return 1/3 * math.pi * self.radius ** 2 * self.height;
  def get_surf(self):
    return math.pi * self.radius ** 2 + math.pi * self.radius * self.height;

small_cone = Cone(40, 50);

print(small_cone.get_surf());
print(small_cone.get_vol());


# ---------------------------

# 두 변의 길이 a,b 와 끼인각 alpha 인 삼각형의 넓이를 구하는 프로그램
import math

a, b = 10, 20;

area = 1 / 2 * a * b * math.sin(math.radians(60))
# 60을 호도법으로 바꿔야 합니다.


print(area);


# ---------------------------


import random;

guess_str = input("1 ~ 45 번호 6개를 쉼표로 분리하여 입력하세요").split(", ")

guess_list = list();
# 공백 list를 하나 생성해 줍니다.

for i in guess_str:
  guess_list.append(int(i));
  

lotto_list = random.sample(range(1, 46, 1), 6)
# 6 개를 랜덤으로 가져옵니다.

print("예상 번호는", guess_list, "입니다.")
print("추첨 번호는", lotto_list, "입니다.");


hit_count = 0;

for guess in guess_list:
  if guess in lotto_list:
    hit_count = hit_count + 1;

print("축하합니다." + str(hit_count) + "개 맞혔습니다.");



# ---------------------------

# 20번의 기회 안에 1 ~ 1000 사이의 숫자를 맞히는 스무고개 프로그램

import random;590

hit_number = random.randint(1, 1001);

guess_count_list = range(1, 21, 1);

passfail = False;

for guess_count in guess_count_list :
  guess = int(input('숫자를 맞혀보세요('+str(guess_count)+'번째 시도)'))

  if hit_number == guess:
    passfail = True;
    break;
  elif hit_number > guess:
    print(str("guess") + "보다 큽니다.", end="")
  else:
    print(str("guess") + "보다 작습니다.", end="")

if passfail == True:
  print("맞혔습니다. 축하합니다.")
else: 
  print("모든 기회를 다 사용했습니다. 다음에 다시 도전하세요.")



# ---------------------------

import time;

def is_prime(x):
  for i in range(2, x):
    if x % i == 0:
      return False;
  return True;

prime_count = 0
# 소수가 몇 개 있는지 카운트하는 변수


# 이거 하다가....