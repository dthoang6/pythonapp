# Give an array of string strs, group the anagrams together. You can return the answer in any oder

# Solution 1: O(m nlogn)
from collections import defaultdict
from typing import List


def group_anagram(strs):
  # Initializing an empty unordered map of a list (a dictionary of a list), which will store the groups of anagrams
  # key is sorting word, and value is list of anagram words
  anagram_map = defaultdict(list) #{key is sorting word: list values of word of same sorting word}

  # Sorting the Word and Grouping the anagram
  for word in strs: # O(m)
    sorted_word = ''.join(sorted(word)) # O(nlogn)
    anagram_map[sorted_word].append(word)
      
  return list(anagram_map.values())

print(group_anagram(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))


def group_anagram1(strs: List[str]) -> List[List[str]]:  # O(mn *26) = O(mn)
  res = defaultdict(list)

  for word in strs: #O(m)
    count = [0] * 26 # a to z # O(26) # for each word we will create an array of 26 character alphabet and count character to do as a key

    for c in word: # O(n)
      count[ord(c) - ord('a')] += 1
    #print(count)
    res[tuple(count)].append(word)
    #print(res.keys())
    #print(res.values())
    #print(res)
    
  return list(res.values())
print(group_anagram1(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
