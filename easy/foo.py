from threading import Event
class Foo(object):
    def __init__(self):
        self.firstDone = Event()
        self.secondDone = Event()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.firstDone.wait()
       
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondDone.set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.secondDone.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.secondDone.set()