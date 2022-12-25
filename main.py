import random

class Cellular_automaton:
    def __init__(self, border, num_of_living):
        self.__border = border
        self.__num_of_living = num_of_living
        self.__field = [' '] * self.__border
        for i in range(self.__border):
            self.__field[i] = [' '] * self.__border
        self.__stock = []

    @property
    def border(self):
        return self.__border
    @property
    def num_of_living(self):
        return self.__num_of_living
    @property
    def field(self):
        return self.__field
    @property
    def stock(self):
        return self.__stock

    @border.setter
    def border(self, border):
        if border < 0:
            print('Ошибка')
        else:
            self.__border = border
    @num_of_living.setter
    def num_of_living(self, num_of_living):
        if num_of_living < 0:
            print('Неправильное количество клеток')
        else:
            self.__border = num_of_living

    def update(self):
        i = 0
        while i != self.__num_of_living:
            x = random.randint(0,self.__border-1)
            y = random.randint(0,self.__border - 1)
            self.__field[x][y] = 1
            i+=1
        render(self.__field)
        while True:
            stop = input('Нажмите любую кнопку, чтобы продолжить, 0 - чтобы выйти из игры: ')
            if stop == '0':
                break
            else:
                self.__stock = [0] * self.__border
                for i in range(self.__border):
                    self.__stock[i] = [0] * self.__border
                self.check_neighbors()
                self.__field = self.__stock
                render(self.__field)

    def check_neighbors(self):
        for i in range(0, self.__border):
            for j in range(0, self.__border):
                check=0
                for x in range(i-1,i+1+1):
                    for y in range(j-1,j+1+1):
                        if x>-1 and y>-1 and x!=self.__border and y!=self.__border and x!=i and y!=j:
                            if self.__field[x][y] == 1:
                                check+=1
                if self.__field[i][j] == 0:
                    if check == 3:
                        self.__stock[i][j] = 1
                    else:
                        self.__stock[i][j] = 0
                else:
                    if check == 2 or check == 3:
                        self.__stock[i][j] = 1
                    else:
                        self.__stock[i][j] = 0

class DLA(Cellular_automaton):
    def __init__(self, border, percent):
        super().__init__(border, percent)

    def update(self):
        self.field[self.border//2][self.border//2] = '#'
        render(self.field)
        while True:
            num_of_ones = 0
            i = random.randint(0, self.border - 1)
            j = random.randint(0, self.border - 1)
            if self.field[i][j] == ' ':
                self.field[i][j] = 1
                render(self.field)
                while self.field[i][j] != '#':
                    self.check_neighbors(i,j)
                    if self.field[i][j] != '#':
                        self.field[i][j] = ' '
                        seed = random.randint(0, 3)
                        if seed == 0:
                            i += 1
                        elif seed == 1:
                            i -= 1
                        elif seed == 2:
                            j += 1
                        elif seed == 3:
                            j -= 1
                        if i == -1 or j == -1 or i == self.border or j == self.border:
                            render(self.field)
                            break
                        else:
                            self.field[i][j] = 1
                    render(self.field)
            for x in range(len(self.field)):
                for y in range(len(self.field[x])):
                    if self.field[x][y] == '#':
                        num_of_ones += 1
            if num_of_ones / (self.border**2) >= self.num_of_living/100:
                break

    def check_neighbors(self, i, j):
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x == -1 or y == -1 or x == self.border or y == self.border or (x!= i and y != j):
                    continue
                if self.field[x][y] == '#':
                    self.field[i][j] = '#'

def render(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end = ' ')
        print()
    print()

def main():
    border = int(input('Введите размер поля: '))
    percent = int(input('Введите процент: '))
    dla = DLA(border, percent)
    dla.update()
main()

