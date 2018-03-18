# Class to create the Observable object for the
# Observable pattern.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Observable(object):
 
    # constructor for Observable class
    def __init__(self):

            # list of observers    
            self.observers = []
 
    # add observer to list of observers
    # @param observer the observer to add
    def add_observer(self, observer):
            if not observer in self.observers:
                    self.observers.append(observer)

    # remove observer from list of observers
    # @param observer the observer to remove
    def remove_observe(self, observer):
            if observer in self.observers:
                    self.observers.remove(observer)
 
    # remove all observers
    def remove_all_observers(self):
            self.observers = []
 
    # update all observers
    # @param arg the arg to send to observer
    def notify_observers(self, arg):
            for observer in self.observers:
                    observer.update(arg)
