from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)
print(q)

p = deque()
p.append(1)
p.appendleft(4)
p.append(3)
print(p)
print(p.pop(), p)
print(p.popleft(), p)
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)

