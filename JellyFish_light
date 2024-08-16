def jelly_light(num, s):
    
    pattern1 = 0  # 010101...
    pattern2 = 0  # 101010...
    
    for i in range(num):
        char1 = '0' if i % 2 == 0 else '1'  
        if s[i] != char1:
            pattern1 += 1
    for j in range(num):
        char2 = '1' if j % 2 == 0 else '0' 
        if s[j] != char2:
            pattern2 += 1
    return min(pattern1, pattern2)
    
num = int(input())
s = input()      
print(jelly_light(num, s))
