from __future__ import annotations
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model

# connection.register_connection("cluster3", session=session)


class FileUpload(Model):
    __key_space__ = "mlspace"
    file_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text()
    active = columns.Text()
    source = columns.Text()
    parameters = columns.Text()
    placement_name = columns.Text()
    effective_from = columns.Text()
    effective_to = columns.Text()
