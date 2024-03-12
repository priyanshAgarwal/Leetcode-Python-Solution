from collections import defaultdict

ans = defaultdict(list)

ans['fruits'].append('apple') 
ans['fruits'].append('banana')
ans['colors'].append('red')

print(ans)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'colors': ['red']})
