class AlphabetIterator:
  def __init__(self, start, stop):
    self.start = start
    self.stop = stop

  def __iter__(self):
    return self

  def __next__(self):
    start = ascii(97)
    stop = ascii(122)
    return self

aLphabet = AlphabetIterator(97, 122)
print(next(aLphabet))
# for num in aLphabet:
#   print(num)