# Justus Perlwitz - https://www.justus.pw/posts/2015-11-30-post.html
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

def probability_distribution(content):
    def _helper():
        absolute_distribution = OrderedCounter(content)
        length = len(content)
        for value, frequency in absolute_distribution.items():
            yield int(value), float(frequency) / length
    return OrderedCounter(dict(_helper()))

with open("ciphertext2", "rb") as fd:
    contents = fd.read()
c = probability_distribution(contents)
max_prob = c.most_common(1)[0][1]
for value, frequency in c.items():
    print("0x{:02x}: {}".format(value, "█" * int(frequency * 80/max_prob)))