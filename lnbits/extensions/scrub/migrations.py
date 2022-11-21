async def m001_initial(db):
    """
    Initial scrub table.
    """
    await db.execute(
        f"""
        CREATE TABLE scrub.scrub_links (
            id TEXT PRIMARY KEY,
            wallet TEXT NOT NULL,
            description TEXT NOT NULL,
            payoraddress TEXT NOT NULL
        );
        """
    )

async def m002_deduct_fee(db):
    """
    Store the multiplier for fiat prices. We store the price in cents and
    remember to multiply by 100 when we use it to convert to Dollars.
    """
    await db.execute(
        "ALTER TABLE scrub.scrub_links ADD COLUMN deduct_fee BOOLEAN DEFAULT FALSE;"
    )
