def generate(val, current, depth, final_list, explored_options):
    print(explored_options, current)
    
    if current in explored_options.keys():
        return explored_options[current]

    if int(val)==int(current):
        final_list.append(depth)
        return depth
    
    if current>=((val+1)*3):
        return -1

    explored_options[current]=-1

    current = current * 2
    result = generate(val, current, depth+1, final_list, explored_options)
    current = int(current/2)
    
    left = current%3
    current=int(current/3)
    result1 = generate(val, current, depth+1, final_list, explored_options)
    current=current*3
    current+=left
    
    if result1<0:
        explored_options[current] = result
    elif result<0:
        explored_options[current] = result1
    else:
        explored_options[current] = min(result, result1)
    
    return explored_options[current]

final = []
generate(10, 1, 0,final, {})
print(min(final))


