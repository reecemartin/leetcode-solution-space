# Failed
def wordBreak1(s: str, wordDict: list[str]) -> bool:
  latest_word = ""
  can_compose = False
  working_s = s
  alternatives = {" ": 0}
  exhausted = False
  attempts = 0

  def otherOptions(s, wordDict):
      other_options = {x for x in wordDict
                       if x.startswith(s)}
      return len(other_options) - 1

  while not exhausted:
    for i in range(len(s)):
        can_compose = False
        latest_word = latest_word + s[i]
        print(latest_word)
        if latest_word in wordDict:
            if otherOptions(latest_word, wordDict) > 0 and latest_word not in alternatives:
                alternatives[latest_word] = otherOptions(latest_word, wordDict)
                print("first round")
                working_s = working_s[i + 1:]
                latest_word = ""
                can_compose = True
            else:
              print("second round")
              if latest_word not in alternatives and otherOptions(latest_word, wordDict) == 0:
                  print("innermost")
                  working_s = working_s[i + 1:]
                  latest_word = ""
                  can_compose = True
    if latest_word == "":
      return True
    elif latest_word == s:
      return False
    else:
      latest_word = ""
      working_s = s
    print(attempts)
    attempts += 1
    if attempts > 5:
      return False
  return can_compose

# ------------------------------------------------------------

# Failed
def wordBreak2(s: str, wordDict: list[str]) -> bool:
  print(wordDict)
  wordSet = set(wordDict)
  all_char_s = set(s)
  all_char_dict = set()
  print(wordSet)
  for word in wordDict:
    all_char_dict = all_char_dict.union(set(word))
  latest_word = ""
  results = []
  longest = max(len(word) for word in wordSet)
  if not all_char_s.issubset(all_char_dict):
    return False

  if s in wordSet:
    return True

  works = set()

################################################################

  def helper(s, wordSet):
    nonlocal works

    print(s, len(s))
    if s in wordSet or s in works:
      return True
    else:
      latest_word = ""
      for i in range(len(s)):
        latest_word += s[i]
        if len(latest_word) > longest:
          return False
        # print("Active")
        if latest_word in wordSet:
          recRes = helper(s[i + 1:], wordSet)
          if recRes:
            works.add(s)
            return True
    return False

  ################################################################

  # for i in range(len(s)):
  #   print("Outer")
  #   latest_word += s[i]
  #   if latest_word in wordSet:
  #     print("Inner")
  #     results.append(helper(s[i + 1:], wordSet))
  # return True in results
  return helper(s, wordSet)

# Passed
def wordBreak(s: str, wordDict: list[str]) -> bool:
  wordDictSorted = sorted(wordDict, key=len, reverse=True)
  print(wordDictSorted)
  results = []
  works = []
  tried = []

  def helper(s):
    print(s)
    nonlocal wordDictSorted
    nonlocal results
    nonlocal works
    nonlocal tried
    if s in wordDictSorted or s in works:
      return True
    for word in wordDictSorted:
      if s.startswith(word):
        if s[len(word):] in wordDictSorted or s[len(word):] in works:
          return True
        if s[len(word):] not in tried:
          result = helper(s[len(word):])
          tried.append(s[len(word):])
          if result:
            works.append(result)
            return True
          results.append(result)
    return True in results

  return helper(s)


print(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))