# -'-coding: euc-kr-'-

from Software import *

sw_list = []

data = Software()

data.set_lecture("�����̽����α׷���", "�����̽����α׷��ֿ� ���� ����.", "1")
sw_list.append(data.lectureList)
data.set_lecture("��ü�������α׷���", "��ü�������α׷��ֿ� ���� ����.", "2")
sw_list.append(data.lectureList)
data.set_lecture("�����������", "����������� ���� ����.", "1")
sw_list.append(data.lectureList)


first_list = []  # 1�г� ����(����, �г�)�� ����ִ� ����Ʈ
second_list = []  # 2�г� ����(����, �г�)�� ����ִ� ����Ʈ
third_list = []  # 3�г� ����(����, �г�)�� ����ִ� ����Ʈ
fourth_list = []  # 4�г� ����(����, �г�)�� ����ִ� ����Ʈ
main_list = []  # main ����Ʈ�� 1,2,3,4�г� ���� �Ϸķ� �� �þ����
final_list = []  # ������ �� �� ��ü ���� ����Ʈ
list1 = []  # ������ �� �� 1�г� ���� ����Ʈ
list2 = []  # ������ �� �� 2�г� ���� ����Ʈ
list3 = []  # ������ �� �� 3�г� ���� ����Ʈ
list4 = []  # ������ �� �� 4�г� ���� ����Ʈ


fileOut = open("test2.txt", 'w')
for i in range(sw_list.__len__()):
    for j in range(3):
        a = sw_list[i][j] + '\n'
        fileOut.write(a)
fileOut.close()


fileIn = open("test2.txt", 'r')
while True:
    line = fileIn.readline()
    if not line:
        break
    print(line.strip('\n'))
fileIn.close()


a = "���α׷���"
# for i in data.lectureList:
for i in range(3):
    if a in sw_list[i][1]:
        if sw_list[i][2] == "1":
            first_list.append([sw_list[i][0], 1])
        elif sw_list[i][2] == "2":
            second_list.append([sw_list[i][0], 2])
        elif sw_list[i][2] == "3":
            third_list.append([sw_list[i][0], 3])
        elif sw_list[i][2] == "4":
            fourth_list.append([sw_list[i][0], 4])

main_list.extend(first_list)
main_list.extend(second_list)
main_list.extend(third_list)
main_list.extend(fourth_list)


# ����Ʈ�� [1] index �� ���Ҹ� �������� ����Ʈ �����ϱ�
for i in range(main_list.__len__()):
    sorted(main_list, key=lambda main: main_list[i][0])

for i in main_list:
    final_list.append(main_list[0])

for i in first_list:
    list1.append(first_list[0])

for i in second_list:
    list2.append(second_list[0])

for i in third_list:
    list3.append(third_list[0])

for i in fourth_list:
    list4.append(fourth_list[0])


print(data.lectureList)
print(sw_list)
print(sw_list[0])
print(first_list)
print(list1)
print(list2)
print(list3)
print(list4)
print(main_list)

