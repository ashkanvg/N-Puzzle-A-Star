from timeit import default_timer


class Tree_Node:
    def __init__(self, data, level, f_score):
        self.data = data
        self.level = level
        self.f_score = f_score

    def generate_child(self):
        x, y = self.find(self.data, '_')
        directions = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in directions:
            child = self.swap(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Tree_Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def swap(self, puzzle, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puzzle = []
            for i in puzzle:
                t = []
                for j in i:
                    t.append(j)
                temp_puzzle.append(t)

            temp = []
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            return temp_puzzle
        else:
            return None

    def find(self, puzzle, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puzzle[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def f_x(self, start, goal):
        # f(x) = h(x) + g(x) 
        return self.h_x(start.data, goal) + start.level

    def h_x(self, start, goal):
        # missplaced
        count = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    count += 1
        return count

    def calculate(self):
        print("Enter the init state matrix:")
        start = []
        for i in range(0, self.n):
            temp = input().split(" ")
            start.append(temp)

        number = 1
        goal = []
        for i in range(0, self.n):
            row = []
            for j in range(0, self.n):
                if (number == self.n * self.n):
                    row.append('_')
                    break
                row.append(str(number))
                number = number + 1
            goal.append(row)

        start = Tree_Node(start, 0, 0)
        start.f_score = self.f_x(start, goal)

        self.open.append(start)

        print("\n")
        print("\033[1;32;40mSECTION 2 - Show States: \033[0;37;40m")
        step = 0
        while True:
            cur = self.open[0]
            print("\033[1mState\033[0m", step, ": ")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            print('f(x) = ' ,self.f_x(cur,goal))
            if (self.h_x(cur.data, goal) == 0):
                break
            for i in cur.generate_child():
                i.f_score = self.f_x(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            step = step + 1
            self.open.sort(key=lambda x: x.f_score, reverse=False)


print("\033[1;32;40m\n\nSECTION 1 - INPUTS: \033[0;37;40m")
# get the size of the puzzle
print("\033[1mEnter the size of the PUZZLE? \033[0m")
print("(3 (8-puzzle),4 (15-puzzle),5 (24-puzzle),...)")
print("(Just enter an Integer number as size of the puzzle. eg. 3 for 3*3 puzzle and 8 puzzle)")
n = int(input())

# create puzzle
puzzle = Puzzle(n)

# start the process of finding solution
start = default_timer()
puzzle.calculate()
end = default_timer()

# show the processing time which calculate by timer
print("\n\033[1mTotal processing time: \033[0m")
print(end - start)

