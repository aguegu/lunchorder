from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
restaurant = Table('restaurant', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=32)),
    Column('telephone', String(length=64), nullable=False),
    Column('address', String(length=128), default=ColumnDefault('')),
    Column('rating', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['restaurant'].columns['title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['restaurant'].columns['title'].drop()
