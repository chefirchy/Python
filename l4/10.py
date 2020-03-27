def print_sequence(n, curr_num = 1, done = 0, done_on_iter = 0):
  if(done_on_iter == curr_num):
    done_on_iter = 0
    curr_num += 1
  if done == n:
    return
  print(curr_num)
  return print_sequence(n, curr_num, done + 1, done_on_iter + 1)


print_sequence(9)