def langton_ant(k):

    grid=[]
    flag=True
    for i in k+1:
        temp=[]
        flag2=flag
        for j in k+1:
            if flag2:
                temp.append(1)
                flag2=not flag2
            else:
                temp.append(0)
                flag2=not flag2
        flag=not flag


    row = k//2
    col = k//2

    direction='UP'
    for i in range(k):
        clock=True
        if grid[row][col]==1:
            clock=True
        else:
            clock=False
        
        if direction=='UP':
            
        