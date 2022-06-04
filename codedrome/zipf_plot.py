from collections import defaultdict
import matplotlib.pyplot as plt

data = open('raw_counts/Oʻtgan kunlar.csv', 'r', encoding="ansi")
r_data = []

# reading relevant data
while True:
    l = data.readline()
    if l == '':
        break
    words = l.split(',')
    wc = (words[0], int(words[1].strip()))
    r_data.append(wc)

d = defaultdict(int)
for k, v in r_data:
    d[k] += v

# sort the list of frequencies in decreasing order
freqs = d.values()
#freqs.sort(reverse=True)
freqs = sorted(freqs, reverse=True)

# enumerate the ranks and frequencies
rf = [(r+1, f) for r, f in enumerate(freqs)]
rs, fs = zip(*rf)

plt.clf()
plt.xscale('log')
plt.yscale('log')
plt.title('Oʻtgan kunlar')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.plot(rs, fs, '.' )
plt.grid()
plt.show()