import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self, **balls):
        self.contents = []
        for key,value in balls.items():
            for x in range(value):
                self.contents.append(key)
        self.backup = copy.deepcopy(self.contents)
    
    def draw(self, n):
        loot = []

        for x in range(n):
            if x >= len(self.backup):
                self.contents = copy.deepcopy(self.backup)
            
            if len(self.contents) == 1:
                loot.append(self.contents.pop())
            else:
                choice = random.randint(0, len(self.contents) - 1)
                loot.append(self.contents.pop(choice))
        
        return loot

    def draw_dict(self, n):
        results = {}
        loot = self.draw(n)
        uniques = set(loot)

        for u in uniques:
            results[u] = loot.count(u)
        return results 
    
    def reset(self):
        self.contents = copy.deepcopy(self.backup)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    count = 0

    for x in range(num_experiments):
        checks = []

        loot = hat.draw_dict(num_balls_drawn)
        hat.reset()

        for key, value in expected_balls.items():
            checks.append(key in loot.keys() and loot[key] >= value)
        
        if all(checks):
            count+= 1

    if count == 0:
        return count
    else:
        return count / num_experiments