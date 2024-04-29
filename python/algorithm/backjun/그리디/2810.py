n = int(input())

seats = input()

seat_cnt = 0
s_cnt = 0
l_cnt = 0
for i in seats:
    if i == 'S':
        s_cnt += 1
    if i == 'L':
        l_cnt += 1

if l_cnt == 0:
    seat_cnt = s_cnt
elif l_cnt == 2:
    seat_cnt = s_cnt + l_cnt
elif l_cnt > 3:
    seat_cnt = s_cnt + (l_cnt - (l_cnt/2 -1) )


print(int(seat_cnt))