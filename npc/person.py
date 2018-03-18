from npc import Npc

class Person(Npc):

    def __init__(self):
        super(Person, self).__init__()
        super(Person, self).set_npc_name('Person')
        super(Person, self).set_npc_hp(100)
        super(Person, self).set_npc_attack(-1)

    def damage_npc(self, player):
        super(Person, self).damage_npc(player)