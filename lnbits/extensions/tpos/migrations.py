from lnbits.db import open_ext_db


def m001_initial(db):
    """
    Initial tposs table.
    """
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS tposs (
            id TEXT PRIMARY KEY,
            wallet TEXT NOT NULL,
            name TEXT NOT NULL,
            currency TEXT NOT NULL
        );
    """
    )


def migrate():
    with open_ext_db("tpos") as db:
        m001_initial(db)