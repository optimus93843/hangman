import os

f_main = open("score_board.txt", "r")
f_temp = open("temp.txt", "a")

username = "hassan"
main_file = {}

for line in f_main:

    (key, val) = line.split(",")
    main_file [key] = int(val[:-1])

print(main_file)

# if username in main_file.keys():
#     main_file[username] += 1
# else:
#     main_file[username] = 1

# print(main_file)

# for user in main_file:
#     f_temp.write(user + ',' + str(main_file[user])+'\n')

# f_temp.close()
# f_main.close()

# os.remove("score_board.txt")
# os.rename("temp.txt","score_board.txt")

