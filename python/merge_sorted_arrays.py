from typing import List
from typing import Optional

# Solution explanation:

# This solution uses the circle list concept to solve this problem. 
# Basically, when we call chainedElement.append(), we add a new element chained to the left element. 

# This solution had performance in O(n), because this code maybe run all lists, but don't do this twice, like in O(n²). However, when we have a simple int, we transform it into a complex object, using more disposable space. So, this solution is not indicated when available space is  no enough.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        rootElement = None
        chainedList = None

        if m > 0:
            rootElement = ChainedElement(previousElement = None, elementValue = nums1.pop(0), nextElement = None)
            m -= 1
        elif m == 0 and n > 0:
            rootElement = ChainedElement(previousElement = None, elementValue = nums2.pop(0), nextElement = None)
            n -= 1
        else:
            return

        chainedList = ChainedList(root = rootElement)

        for i in range(max(m,n)):
            if i < m:
                element = ChainedElement(previousElement = None, elementValue = nums1.pop(0), nextElement = None)
                chainedList.append(element)
            if i < n:
                element = ChainedElement(previousElement = None, elementValue = nums2.pop(0), nextElement = None)
                chainedList.append(element)
        
        nums1.clear()
        nums2.clear()

        chainedList.toList(chainedList = nums1)

class ChainedElement:
    def __init__ (self: "ChainedElement", previousElement: Optional["ChainedElement"], elementValue: int, nextElement: Optional["ChainedElement"]):
        self.previousElement = previousElement
        self.elementValue = elementValue
        self.nextElement = nextElement

        
class ChainedList:
    def __init__(self: "ChainedList", root: "ChainedElement"):
        self.root = root
        self.count = 0

    def __tryNextPosition__(self: "ChainedList", currentElement: "ChainedElement", elementToAppend: "ChainedElement"):
        nextElement = currentElement.nextElement
        if elementToAppend.elementValue >= currentElement.elementValue and elementToAppend.elementValue < nextElement.elementValue:
            elementToAppend.previousElement = currentElement
            elementToAppend.nextElement = nextElement
            currentElement.nextElement = elementToAppend
            nextElement.previousElement = elementToAppend
        else: 
            self.__tryNextPosition__(currentElement = currentElement.nextElement, elementToAppend = elementToAppend)

    def __isLastItemNone__(self: "ChainedList", last: "ChainedElement", element: "ChainedElement") -> bool:
        if (last == None):
            if self.root.elementValue <= element.elementValue:
                element.nextElement = self.root
                element.previousElement = self.root
                self.root.nextElement = element
                self.root.previousElement = element
            else:
                lastRoot = self.root
                element.nextElement = lastRoot
                element.previousElement = lastRoot
                self.root = element
                lastRoot.nextElement = self.root
                lastRoot.previousElement = self.root
            return True
        else: return False

    def __getNextElement__(self: "ChainedList", chainedList: List[int], element: "ChainedElement", count: int):
        chainedList.append(element.elementValue)
        if count == self.count: return
        else: self.__getNextElement__(chainedList = chainedList, element = element.nextElement, count = count + 1)

    def append(self: "ChainedList", element: "ChainedElement"):
        self.count += 1
        last = self.root.previousElement
        if self.__isLastItemNone__(last = last, element = element):
            return
        elif last.elementValue <= element.elementValue:
            element.previousElement = last
            element.nextElement = self.root
            self.root.previousElement = element
            last.nextElement = element
        elif self.root.elementValue >= element.elementValue:
            element.nextElement = self.root
            element.previousElement = last
            last.nextElement = element
            self.root = element
        else: self.__tryNextPosition__(currentElement = self.root, elementToAppend = element)

    def toList(self: "ChainedList", chainedList: List[int]):
        self.__getNextElement__(chainedList = chainedList, element = self.root, count = 0)

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
Solution().merge(nums1 = nums1, m=m, nums2 = nums2, n = n)
print(nums1)