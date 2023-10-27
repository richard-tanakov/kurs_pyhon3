istr = input()
nmax = 0
chmax = '\0'
n = 1
pch = '\0'
for ch in istr:
  if ch != pch:
    n = 1
  if n >= nmax:
    chmax = ch
    nmax = n
  pch = ch
  n += 1

print(chmax)
print(nmax)