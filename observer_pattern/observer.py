from abc import ABCMeta, abstractmethod

# Abstract Obsever class to observer pattern.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Observer(object):
    __metaclass__ = ABCMeta
 
    # method to update observer
    # @param arg the arg that was sent by observable        
    @abstractmethod
    def update(self, arg):
        pass