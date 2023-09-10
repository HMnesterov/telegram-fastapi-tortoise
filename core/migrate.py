import os
from typing import List
from core.logger import logger
from core.settings import settings
from tortoise import fields, models
from tortoise.transactions import in_transaction


class Migrate(models.Model):
    id = fields.BigIntField(pk=True)
    file = fields.CharField(max_length=1024)


async def migrate():
    #create migration table
    async with in_transaction("default") as conn:
        await conn.execute_script(
            "create table if not exists \"migrate\"(\"id\" BIGSERIAL PRIMARY KEY, \"file\" varchar(1024));"
        )
    #collect new migrations
    scripts_files: List[str] = os.listdir(settings.DB_MIGRATE_PATH)
    if not scripts_files:
        return
    script_db: Migrate = await Migrate.filter().order_by('-id').first()
    if script_db is None:
        unregistered_migration_scripts = scripts_files
    else:
        unregistered_migration_scripts = scripts_files[scripts_files.index(script_db.file) + 1:]
    #make migrations
    logger.info(msg=f"Found {len(unregistered_migration_scripts)} changes: {unregistered_migration_scripts}")
    for migration_script in unregistered_migration_scripts:
        async with in_transaction("default") as t_conn:
            sql_script = open(file=f"{settings.DB_MIGRATE_PATH}{os.sep}{migration_script}", mode="r").read()
            await t_conn.execute_script(sql_script)
            await Migrate.create(file=migration_script)



