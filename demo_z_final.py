import random

g = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

def display(g, score):
        print('{0:4} {1:4} {2:4} {3:4}'.format(g[0][0], g[0][1], g[0][2], g[0][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(g[1][0], g[1][1], g[1][2], g[1][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(g[2][0], g[2][1], g[2][2], g[2][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(g[3][0], g[3][1], g[3][2], g[3][3]), '    Total score: ', score)

def init(g):
    for i in range(4):
                g[i] = [random.choice([0, 0, 0, 0, 2, 4]) for x in range(4)]

def align(gList, direction):
        for i in range(gList.count(0)):
            gList.remove(0)
        zeros = [0 for x in range(4 - len(gList))]
        if direction == 'left':
                gList.extend(zeros)
        else:
                gList[:0] = zeros
        
def addSame(gList, direction):
        score = 0
        if direction == 'left':
                for i in [0, 1, 2]:
                        if gList[i] == gList[i+1] != 0: 
                                gList[i] *= 2
                                gList[i+1] = 0
                                score += gList[i]
                                return {'bool':True, 'score':score}
        else:
                for i in [3, 2, 1]:
                        if gList[i] == gList[i-1] != 0:
                                gList[i-1] *= 2
                                gList[i] = 0
                                score += gList[i-1]
                                return {'bool':True, 'score':score}
        return {'bool':False, 'score':score}

def handle(gList, direction):
        totalScore = 0
        align(gList, direction)
        result = addSame(gList, direction)
        while result['bool'] == True:
                totalScore += result['score']
                align(gList, direction)
                result = addSame(gList, direction)
        return totalScore
      
def operation(g):
        totalScore = 0
        gameOver = False
        direction = 'left'
        op = input('operator:')
        if op in ['a', 'A']: 
                direction = 'left'
                for row in range(4):
                        totalScore += handle(g[row], direction)
        elif op in ['d', 'D']:
                direction = 'right'
                for row in range(4):
                        totalScore += handle(g[row], direction)
        elif op in ['w', 'W']:
                direction = 'left'
                for col in range(4):
                        gList = [g[row][col] for row in range(4)]
                        totalScore += handle(gList, direction)
                        for row in range(4):
                                g[row][col] = gList[row]
        elif op in ['s', 'S']: 
                direction = 'right'
                for col in range(4):
                        gList = [g[row][col] for row in range(4)]
                        totalScore += handle(gList, direction)
                        for row in range(4):
                                g[row][col] = gList[row]
        else:
                print('Invalid input, please enter a charactor in [W, S, A, D] or the lower')
                return {'gameOver':gameOver, 'score':totalScore}
        N = 0
        for q in g:
            N += q.count(0)
        if N == 0:
                gameOver = True
                return {'gameOver':gameOver, 'score':totalScore}
        num = random.choice([0,0,2,4]) 
        k = random.randrange(1, N+1)
        n = 0
        for i in range(4):
                for j in range(4):
                        if g[i][j] == 0:
                                n += 1
                                if n == k:
                                        g[i][j] = num
                                        break
        return {'gameOver':gameOver, 'score':totalScore}

init(g)
score = 0
print('Input：W(Up) S(Down) A(Left) D(Right), press <CR>.')
while True:
        display(g, score)
        result = operation(g)
        if result['gameOver'] == True:
                print('Game Over, You failed!')
                print('Your total score:', score)
        else:
                score += result['score']
                if score >= 2048:
                        print('Game Over, You Win!!!')
                        print('Your total score:', score)