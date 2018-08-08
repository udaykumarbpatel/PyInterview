ip = 6
log = ["mi2 Jog mid pet", "wz3 34 54 398", "1a alps cow bar", "x4 45 21 7", "1C alps cow bar", "az4 34 54 398"]

def solution(log):
  res_W = []
  res_N = []
  for line in log:
    words = line.split(' ')
    id, li = words[0],words[1:]
    if check_all_nos(li):
      res_N.append(line)
    else:
      res_W.append(line)
  res_W = custom_sort(res_W)
  res_W.extend(res_N)
  return res_W

def check_all_nos(lst):
  for x in lst:
    if not x.isdigit():
      return False
  return True

def s(data):
    return sorted(data, key=lambda item: (int(item.partition(' ')[0]) if item[0].isdigit() else float('inf'), item))

def custom_sort(lst):
  map = {}
  rev_map = {}
  new_lst = []
  old_lst = []
  for item in lst:
    words = item.split(' ')
    id = words[0]
    map[id] = ' '.join(words)
    words = words[1:]
    words = ''.join(words)
    if words in rev_map:
        _lst = rev_map[words]
        _lst.append(id)
        rev_map[words] = sorted(_lst)
    else:
        rev_map[words] = [id]

    new_lst.append(words)
  new_lst = s(list(set(new_lst)))
  for item in new_lst:
    ids = rev_map[item]
    for id in ids:
        words = map[id]
        old_lst.append(words)
  return old_lst



print solution(log)
