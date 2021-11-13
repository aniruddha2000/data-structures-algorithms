class NodeTree(object):
    def __init__(self, left=None, right=None) -> None:
        self.left = left
        self.right = right

    def child(self) -> object:
        return (self.left, self.right)

    def nodes(self) -> object:
        return (self.left, self.right)

    def __str__(self) -> str:
        return "%s_%s" % (self.left, self.right)


class HuffManCoding:
    def __init__(self, msg) -> None:
        self.msg = msg

    def HuffManCodingTree(self, node, left=True, codeString="") -> dict:
        if type(node) is str:
            return {node: codeString}
        (l, r) = node.child()
        d = dict()
        d.update(self.HuffManCodingTree(l, True, codeString + "0"))
        d.update(self.HuffManCodingTree(r, False, codeString + "1"))
        return d

    def frequencyCalculate(self, msg) -> dict:
        freq = {}
        for c in msg:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq

    def createTree(self):
        freq = self.frequencyCalculate(self.msg)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])

        nodes = sorted_freq
        while len(nodes) > 1:
            (key1, val1) = nodes[0]
            (key2, val2) = nodes[1]
            nodes = nodes[2:]
            newNode = NodeTree(key1, key2)
            nodes.append((newNode, val1 + val2))
            nodes = sorted(nodes, key=lambda x: x[1])
        huffmanCode = self.HuffManCodingTree(nodes[0][0])
        return huffmanCode, sorted_freq, nodes[0][0]

    def printCodedStringTable(self) -> None:
        huffManCode, freq, _ = self.createTree()
        for (char, frequency) in freq:
            print(" %-4r |%12s" % (char, huffManCode[char]))

    def printCodedString(self) -> None:
        huffManCode, _, _ = self.createTree()
        print("Original Messege: ")
        print(self.msg)
        print("Encoded String: ")
        for s in self.msg:
            print(huffManCode[s], end="")
        print()

    def getTreeHead(self):
        _, _, treeHead = self.createTree()
        return treeHead


testCase1 = "BCAADDDCCACACAC"
decode = HuffManCoding(testCase1)
decode.printCodedStringTable()
decode.printCodedString()
testCase1_TreeHead = decode.getTreeHead()
