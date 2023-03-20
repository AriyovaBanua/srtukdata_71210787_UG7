class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def go(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()

    def back(self):
        if len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            return self.back_stack[-1]

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.forward_stack.pop())
            return self.back_stack[-1]

    def printAll(self):
        print(*self.back_stack)


browser = Browser()

browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")

print(browser.back()) 
print(browser.back())
print(browser.forward())

browser.go("https://twitter.com") 

browser.printAll()