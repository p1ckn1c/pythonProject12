FIELD = []
a = [[(lambda x: 0 if x % 2 == 0 else 1)(i) for i in range(j, j + 8)] for j in range(8)]
for item in a:
    f = 0
    for i in item:
        FIELD.append(f'{str(0)}')


class Field:
    def __init__(self, field):
        self.field = field

    def fill(self, num, symbol):
        self.field[num] = symbol

    def __repr__(self):
        f = self.field
        return f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[0]}\t|\t{f[1]}\t|\t{f[2]}\t|\t{f[3]}\t|\t{f[4]}\t|\t{f[5]}\t|\t{f[6]}\t|\t{f[7]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[8]}\t|\t{f[9]}\t|\t{f[10]}\t|\t{f[11]}\t|\t{f[12]}\t|\t{f[13]}\t|\t{f[14]}\t|\t{f[15]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[16]}\t|\t{f[17]}\t|\t{f[18]}\t|\t{f[19]}\t|\t{f[20]}\t|\t{f[21]}\t|\t{f[22]}\t|\t{f[23]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[24]}\t|\t{f[25]}\t|\t{f[26]}\t|\t{f[27]}\t|\t{f[28]}\t|\t{f[29]}\t|\t{f[30]}\t|\t{f[31]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[32]}\t|\t{f[33]}\t|\t{f[34]}\t|\t{f[35]}\t|\t{f[36]}\t|\t{f[37]}\t|\t{f[38]}\t|\t{f[39]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[40]}\t|\t{f[41]}\t|\t{f[42]}\t|\t{f[43]}\t|\t{f[44]}\t|\t{f[45]}\t|\t{f[46]}\t|\t{f[47]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[48]}\t|\t{f[49]}\t|\t{f[50]}\t|\t{f[51]}\t|\t{f[52]}\t|\t{f[53]}\t|\t{f[54]}\t|\t{f[55]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \
               f'|\t{f[56]}\t|\t{f[57]}\t|\t{f[58]}\t|\t{f[59]}\t|\t{f[60]}\t|\t{f[61]}\t|\t{f[62]}\t|\t{f[63]}\t|\n' \
               f'*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\t-\t*\n' \


def main():
    field = Field(FIELD)
    print(field)
    user_input1 = input("Привет!\n"
                        "0 - означает клетку\n"
                        "p - означает пустую клетку\n"
                        "Выберите чем вы будет отмечать клетки\n")
    user_input2 = input("Выберите чем вы будет отмечать клетки в которых как вы думаете есть бомба\n")
    print(field)
    sc = 0
    while True:
        user_input = int(input("Выберете ячейку: "))
        answer = input("Введите:\n"
                       f"0 - хотите отметить ячейку знаком {user_input1}\n"
                       f"1 - хотите отметить ячейку знаком {user_input2}\n")
        if answer == '0':
            i = user_input - 1
            s = 'p'
            s1 = '1'
            s2 = '2'
            s3 = '3'
            s4 = '4'
            if (i == 16) or (i == 24) or (i == 25) or (i == 26) or (i == 32) or (i == 33) or (i == 34) or (i == 40) or (
                    i == 41) or (i == 42) or (i == 51) or (i == 59) or (i == 8) or (i == 9) or (i == 17) or (
                    i == 18) or (i == 19) or (i == 27) or (i == 35) or (i == 43) or (i == 48) or (i == 49) or (
                    i == 50) or (i == 44) or (i == 52) or (i == 58) or (i == 60):
                field.fill(16, s)
                field.fill(24, s)
                field.fill(25, s)
                field.fill(26, s)
                field.fill(32, s)
                field.fill(33, s)
                field.fill(34, s)
                field.fill(40, s)
                field.fill(41, s)
                field.fill(42, s)
                field.fill(8, s1)
                field.fill(17, s1)
                field.fill(18, s1)
                field.fill(27, s1)
                field.fill(35, s1)
                field.fill(43, s1)
                field.fill(48, s1)
                field.fill(49, s1)
                field.fill(50, s1)
                field.fill(9, s2)
                field.fill(19, s2)
                field.fill(51, s)
                field.fill(59, s)
                field.fill(58, s1)
                field.fill(60, s1)
                field.fill(52, s1)
                field.fill(44, s1)
                print(field)
            elif (i == 30) or (i == 31) or (i == 38) or (i == 39):
                field.fill(30, s)
                field.fill(31, s)
                field.fill(38, s)
                field.fill(39, s)
                field.fill(29, s1)
                field.fill(37, s1)
                field.fill(45, s1)
                field.fill(46, s1)
                field.fill(47, s1)
                field.fill(23, s2)
                field.fill(22, s2)
                field.fill(21, s2)
                print(field)
            elif (i == 1) or (i == 3) or (i == 7) or (i == 9) or (i == 11) or (i == 19) or (i == 21) or (i == 22) or (
                    i == 23) or (i == 53):
                field.fill(i, s2)
                print(field)
            elif (i == 6) or (i == 13):
                field.fill(i, s3)
                print(field)
            elif i == 54:
                field.fill(i, s3)
                print(field)
            elif (i == 8) or (i == 2) or (i == 4) or (i == 17) or (i == 18) or (i == 20) or (i == 29) or (i == 28) or (
                    i == 27) or (i == 37) or (i == 35) or (i == 43) or (i == 44) or (i == 45) or (i == 46) or (
                    i == 47) or (i == 48) or (i == 49) or (i == 50) or (i == 52) or (i == 56) or (i == 58) or (i == 60):
                field.fill(i, s1)
                print(field)
            elif (i == 0) or (i == 5) or (i == 10) or (
                    i == 15) or (i == 14) or (i == 16) or (
                    i == 55) or (i == 57) or (i == 63) or (
                    i == 62) or (i == 61):
                text2 = 'Вы проиграли'
                print("\033[31m {}".format(text2))
                exit()
        elif answer == '1':
            i = user_input - 1
            field.fill(i, user_input2)
            print(field)
            if (i == 0) or (i == 5) or (i == 10) or (i == 14) or (i == 15) or (i == 36) or (i == 55) or (i == 57) or (
                    i == 61) or (i == 62) or (i == 63) or (i == 12):
                sc += 1
                if sc == 12:
                    text1 = 'Вы выиграли'
                    print("\033[32m {}".format(text1))
                    exit()


if __name__ == "__main__":
    main()
