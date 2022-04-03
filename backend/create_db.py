from cassandra.cluster import Cluster

clstr = Cluster()
session = clstr.connect()


# creating a keyspace
# session.execute(
#     "create keyspace mlkeyspace with replication={ 'class': 'SimpleStrategy', 'replication_factor' : 3};"
# )

# connecting the database
session = clstr.connect("mlkeyspace")


# creating the table
qry = """
create table FileUpload (
   file_id text,
   name text,
   active text,
   source text,
   parameters text,
   placement_name text,
   effective_from text,
   effective_to text,
   primary key(file_id)
);"""

qry1_delete = """
drop table FileUpload;
"""

qry2 = """
create table Streaming (
   streaming_id text,
   name text,
   ip_address text,
   nic text,
   username text,
   password text,
   parameters text,
   placement_name text,
   effective_from text,
   effective_to text,
   active text,
   primary key(streaming_id)
);
"""

qry2_delete = """
   drop table FileUpload;
"""


qry3 = """
create table DBPull (
   pull_id text,
   name text,
   source text,
   port text,
   parameters text,
   placement_name text,
   effective_from text,
   effective_to text,
   active text,
   primary key(pull_id)
);
"""


qry3_delete = """
   drop table FileUpload;
"""

from Source.migration.migration import Migration


import sys

if __name__ == "__main__":
    try:
        name = sys.argv[1]
        try:
            table = sys.argv[2]
            if table == "_all_":
                m = Migration()
                if name == "upgrade":
                    m.upgrade(session, qry)
                    m.upgrade(session, qry2)
                    m.upgrade(session, qry3)
                else:
                    m.downgrade(session, qry1_delete)
                    m.downgrade(session, qry2_delete)
                    m.downgrade(session, qry3_delete)

        except Exception:
            print("No table name passed")
    except Exception:
        print("pass parameters upgrade or downgrade and table name")
