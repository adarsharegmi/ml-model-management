from cassandra.cluster import Cluster


from cassandra.cluster import Cluster

clstr = Cluster()
session = clstr.connect()


class DbConnection():
    def execute(self, query, values=None):
        session.execute(query)

    async def execute_many(self, query, values):
        raise NotImplementedError()

    async def fetch_all(self, query):
        raise NotImplementedError()

    async def fetch_one(self, query):
        raise NotImplementedError()

    async def fetch_val(self, query):
        raise NotImplementedError()
