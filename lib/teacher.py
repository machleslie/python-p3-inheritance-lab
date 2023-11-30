#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    knowledge = []
    knowledge.append(random)

    def teach(self):
        random_index = random.randint(0, len(self.knowledge) - 1)
        print (self.knowledge[random_index])

t=Teacher("my","teacher")
t.teach()