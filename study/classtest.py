# -*-coding:utf-8 -*-
#print "中文"
#answer_yes = ['yes','YES','y','Y']
#if raw_input('请输入是否继续') in answer_yes:
#    print 'OK'
#else:
  #  print 'Next'

class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world! I'm %s." %self.name

foo = Person()
foo.setName('Luke skywalker')
foo.greet()
print foo.name
Person.greet(foo)
print Person.getName(foo)
