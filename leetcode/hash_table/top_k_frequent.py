#
def top_k_frequent(nums, k):
  frequent_table = {}
  most_fre = []
  for num in nums:
    if num in frequent_table:
      frequent_table[num] += 1
    else:
      frequent_table[num] = 1

  #print(frequent_table)
  #print(frequent_table.keys())
  #print(frequent_table.values())
  for x in frequent_table:
    if frequent_table[x] >= k:
      most_fre.append(x)

  return most_fre

nums = [1, 1, 1, 2, 2, 3]

print(top_k_frequent(nums, 2))
print(top_k_frequent([1,2,4,1,5,7,6,5,8,2,1], 1))
print(top_k_frequent([1,2,4,1,5,7,6,5,8,2,1], 3))