class DynamicCypher(CypherDescription):
    @property
    def might_pool(self):
        math.rand(0, 10)


Fury = DynamicCypher()
Fury.might_pool