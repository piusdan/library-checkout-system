# /library-checkout-system/library-checkout-system/alembic/env.py

"""
Alembic environment configuration file.
"""

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Import the database models
from app.models import author
from app.models import book
from app.models import checkout

# Import the database connection
from app.database import engine

# Configure the Alembic config
config = context.config

# Set the target metadata
target_metadata = [author.Base.metadata, book.Base.metadata, checkout.Base.metadata]

# Configure the database connection
config.set_main_option("sqlalchemy.url", str(engine.url))

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Initialize the Alembic environment
def run_migrations_offline():
    """
    Run migrations in 'offline' mode.
    """
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """
    Run migrations in 'online' mode.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

# Run migrations based on the context
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()