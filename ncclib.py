from itertools import product

class Generate:
    def __init__(self):
        self.binList=[]
        self.charList=[] #all character including special characters

    #input binary string will return binary list eg:binary=['0','1']
    def generatebin(self,binary):
        """
        This method will return binary list using length of character list (self.charList)
        :param binary:
        :return: The return range is 0:len(self.generateChar())-1
        """
        for i in product(binary, binary, binary, binary, binary, binary, binary):
            self.binList.append(int(self.toString(i)))
        return self.binList[0:len(self.generateChar())-1]

    def toString(self,mytuple):
        """
        This method used to change tuple to string
        :param mytuple:
        :return: string
        """
        a = ''
        for i in mytuple:
            a = a + i
        return a
    def generateChar(self):
        for i in range(32, 127):
            # print(chr(i),end=" ")
            self.charList.append(str(chr(i)))
        return self.charList


if __name__ == '__main__':
    binary=['0','1']
    oGenerate:Generate=Generate()
    binary_list = oGenerate.generatebin(binary)

    print(binary_list,len(binary_list))

    print("charlist\n",oGenerate.charList)
