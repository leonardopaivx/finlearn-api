import sqlalchemy as sa


class Audits:
    date_created = sa.Column(
        sa.TIMESTAMP(timezone=True), server_default=sa.sql.func.now()
    )
    date_updated = sa.Column(
        sa.TIMESTAMP(timezone=True),
        server_default=sa.sql.func.now(),
        onupdate=sa.sql.func.now(),
    )
