class Migration:
    def __init__(self) -> None:
        pass

    def upgrade(self, session, query) -> bool:
        try:
            session.execute(query)
            return True
        except Exception:
            "the code here is for updating the column names, type in table pending"
            return False

    def downgrade(self, session, table) -> None:
        try:
            # "Drop if exists"
            session.execute("Drop table", table)
        except Exception:
            print("No table exists")
