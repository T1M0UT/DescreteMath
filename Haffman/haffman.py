# from copy import copy


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


def calculate_probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


codes = dict()
def calculate_codes(node: Node, val=''):
    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)
    if not node.left and not node.right:
        codes[node.symbol] = newVal

    return codes


def output_encoded(data, coding, display=False):
    encoding_output = []
    for char in data:
        if display:
            print(coding[char], end='')
        encoding_output.append(coding[char])

    string = ''.join([str(item) for item in encoding_output])
    return string


def total_gain(data, coding):
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])
    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):", after_compression)


def huffman_encoding(data):
    symbol_with_probs = calculate_probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols:", symbols)
    print("probabilities:", probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append((Node(symbol_with_probs.get(symbol), symbol)))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calculate_codes(nodes[0])
    print(huffman_encoding)
    total_gain(data, huffman_encoding)
    encoded_output = output_encoded(data, huffman_encoding)
    print("Encoded output:", encoded_output)
    return encoded_output, nodes[0]


if __name__ == "__main__":
    huffman_encoding("THIS IS A SIMPLE EXAMPLE OF HUFFMAN ENCODING")
    huffman_encoding("МІНІМІЗАЦІЯ ЧАСУ ВИКОНАННЯ ПРОГРАМИ")
