# 6) Huffman Coding (Greedy Algorithm)

chars = ["a", "b", "c", "d", "e", "f"]
freq = [5, 9, 12, 13, 16, 45]

print("Characters:", chars)
print("Frequencies:", freq)

# Each node: character, frequency, left, right
nodes = []
for i in range(len(chars)):
    nodes.append({"ch": chars[i], "freq": freq[i], "left": None, "right": None})

# Build Huffman tree by combining two minimum frequency nodes
while len(nodes) > 1:
    nodes.sort(key=lambda x: x["freq"])
    left = nodes[0]
    right = nodes[1]
    new_node = {
        "ch": left["ch"] + right["ch"],
        "freq": left["freq"] + right["freq"],
        "left": left,
        "right": right,
    }
    print("Combine", left["ch"], "and", right["ch"], "-> freq", new_node["freq"])
    nodes.pop(0)
    nodes.pop(0)
    nodes.append(new_node)

root = nodes[0]
codes = {}


def generate_codes(node, code):
    if node is None:
        return
    if node["left"] is None and node["right"] is None:
        codes[node["ch"]] = code
        return
    generate_codes(node["left"], code + "0")
    generate_codes(node["right"], code + "1")


generate_codes(root, "")

print("Huffman Codes:")
for ch in chars:
    print(ch, ":", codes[ch])
