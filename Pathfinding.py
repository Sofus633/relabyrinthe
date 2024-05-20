
def path(enemypos, plapos, board):
    results = [[enemypos[0] + 1, enemypos[1]], [enemypos[0], enemypos[1] + 1], [enemypos[0]- 1, enemypos[1]], [enemypos[0], enemypos[1] - 1]]
    distance = []
    i = 0
    for pos in results:
        i += 1
        if board[pos[0] - plapos[0]][pos[1] - plapos[1]] != 1:
            
            distance.append([abs(pos[0] - plapos[0]) + abs(pos[1] - plapos[1]), i])
        
    plsg = distance[0][0]
    for a in distance:
        if a[0] > plsg:
            plsg = a[0]
    
    return plsg