class CypherDescriptor:
    def __init__(self, descriptor):
        self.descriptor = descriptor
        self.description = None
        self.might_pool_mod = 0
        self.might_edge_mod = 0
        self.speed_pool_mod = 0
        self.speed_edge_mod = 0
        self.intellect_pool_mod = 0
        self.intellect_edge_mod = 0
        self.inabilities = None
        self.skill = None

    def descriptor_getter(self):
        return self.descriptor

    def descriptor_setter(self, new_descriptor):
        self.descriptor = new_descriptor

    def description_getter(self):
        return self.description

    def description_setter(self, new_description):
        self.description = new_description

    def might_pool_getter(self):
        return self.might_pool_mod

    def might_pool_setter(self, new_might_pool):
        self.might_pool_mod = new_might_pool

    def intellect_pool_getter(self):
        return self.intellect_pool_mod

    def intellect_pool_setter(self, new_intellect_pool):
        self.intellect_pool_mod = new_intellect_pool

    def speed_pool_getter(self):
        return self.speed_pool_mod

    def speed_pool_setter(self, new_speed_pool):
        self.speed_pool_mod = new_speed_pool

    def might_edge_getter(self):
        return self.might_edge_mod

    def might_edge_setter(self, new_might_edge):
        self.might_edge_mod = new_might_edge

    def speed_edge_getter(self):
        return self.speed_edge_mod

    def speed_edge_setter(self, new_speed_edge):
        self.speed_edge_mod = new_speed_edge

    def intellect_edge_getter(self):
        return self.intellect_edge_mod

    def intellect_edge_setter(self, new_intellect_edge):
        self.intellect_edge_mod = new_intellect_edge

    def inabilities_getter(self):
        return self.inabilities

    def inabilities_setter(self, new_inabilities):
        self.inabilities = new_inabilities

    def skill_getter(self):
        return self.skill

    def skill_setter(self, new_skill):
        self.skill = new_skill

Descriptors = {}

Brash = CypherDescriptor('Brash')
Brash.description = """
You’re a self-assertive sort, confident in your abilities, energetic, and perhaps a bit irreverent toward ideas that you don’t agree with. Some people call you bold and brave, but those you’ve put in their place might call you puffed up and arrogant. Whatever. It’s not in your nature to care what other people think about you, unless those people are your friends or family. Even someone as brash as you knows that friends sometimes have to come first.
"""
Brash.speed_pool_setter(1)
Brash.intellect_pool_setter(1)
Descriptors['brash'] = Brash

Descriptors['something_else'] = CypherDescriptor('something_else')


