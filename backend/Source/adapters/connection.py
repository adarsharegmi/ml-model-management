from cassandra.cqlengine.connection import setup
from cassandra.cqlengine.management import sync_table
from Source.adapters.orm import FileUpload


def cass_connect():
    setup(["127.0.0.1"], "mlkeyspace", retry_connect=True)
    sync_table(FileUpload)


def get_connection():
    """
    returns the database connection for working purpose
    """
    return cass_connect()
