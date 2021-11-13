from huffmanCoding import testCase1_TreeHead


class HuffmanDecoding:
    def __init__(self, msg, treeHead) -> None:
        self.encoded_msg = msg
        self.treeHead = treeHead

    def printDecodedString(self):
        decodedString = self.huffmanDecoding(self.encoded_msg, self.treeHead)
        print("Decoded String :")
        print(decodedString)

    def huffmanDecoding(self, encoded_msg, treeHead):
        tmp_tree = treeHead
        decodedString = ""
        for data in encoded_msg:
            if data == "1":
                tmp_tree = tmp_tree.right
            elif data == "0":
                tmp_tree = tmp_tree.left

            if isinstance(tmp_tree, str):
                decodedString += tmp_tree
                tmp_tree = treeHead
            else:
                continue
        return decodedString


testCase = "1000111110110110100110110110"
treeHead = testCase1_TreeHead
decode = HuffmanDecoding(testCase, treeHead)
decode.printDecodedString()
