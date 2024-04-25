# This program will return true if input array of integer contain duplicate, otherwise return false

def contain_duplicate(nums):
  hash_table = {}
  if len(nums) < 2:
    return False
  
  for num in nums:
    if num in hash_table:
      print(hash_table)
      return True
    else:
      hash_table.update({num : False})
      print(hash_table)
  
  return False

def main():
  nums1 = [1, 2, 3, 4]
  nums2 = [1, 2, 1, 2]
  nums3 = [1, 2, 1]

  #print(contain_duplicate(nums1))
  #print(contain_duplicate(nums2))
  print(contain_duplicate(nums3))

main()