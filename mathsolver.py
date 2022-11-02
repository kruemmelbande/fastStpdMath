
class stack:
    def __init__(self) -> None:
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def getAll(self):
        return self.stack
    def top(self):
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    def clear(self):
        self.stack = []

class queue:
    def __init__(self) -> None:
        self.queue = []
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        return self.queue.pop(0)
    def top(self):
        return self.queue[0]
    def getAll(self):
        return self.queue
    def isEmpty(self):
        return self.queue == []
    def clear(self):
        self.queue = []

def cut(input:str,toRemove:str):
    working=input.strip()
    if working[:len(toRemove)] == toRemove:
        return working[len(toRemove):].strip()

def solveMath(equasion):
    q=queue()
    s=stack()
    seperated=queue()
    operators=["+","-","*","/","^","(",")","<<",">>","==","!=","<=",">="]
    wequasion=equasion.replace(" ","")
    while wequasion != "":
        if wequasion.startswith("("):
            seperated.push("(")
            wequasion=cut(wequasion,"(")
            continue
        if wequasion.startswith(")"):
            seperated.push(")")
            wequasion=cut(wequasion,")")
            continue
        if wequasion.startswith("-"):
            w=""
            i=1
            while wequasion[i].isdigit() or wequasion[i]==".":
                w+=wequasion[i]
                i+=1
                if i==len(wequasion):
                    break
            seperated.push(-float(w))
            wequasion=cut(wequasion,"-"+w)
            continue
        for i in range(len(wequasion)):
            for k in operators:
                if wequasion[i:].startswith(k):
                    seperated.push(wequasion[:i])
                    seperated.push(k)
                    wequasion=cut(wequasion,wequasion[:i]+k)
        for k in operators:
            if k in wequasion:
                break
        else:
            seperated.push(wequasion)
            break
    print(seperated.getAll())
if __name__=="__main__":
    print(solveMath(input("uwu: ")))