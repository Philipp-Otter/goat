"""Addded sensitity field

Revision ID: 910f067bbf0b
Revises: 829c4e15556f
Create Date: 2022-04-20 14:46:52.964304

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import sqlmodel  

from alembic_utils.pg_grant_table import PGGrantTable
from sqlalchemy import text as sql_text

# revision identifiers, used by Alembic.
revision = '910f067bbf0b'
down_revision = '829c4e15556f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poi_default_config', sa.Column('sensitivity', sa.Integer(), nullable=True), schema='basic')
    op.drop_constraint('poi_default_config_group_fkey', 'poi_default_config', schema='basic', type_='foreignkey')
    op.add_column('poi_study_area_config', sa.Column('sensitivity', sa.Integer(), nullable=True), schema='basic')
    op.drop_constraint('poi_study_area_config_group_fkey', 'poi_study_area_config', schema='basic', type_='foreignkey')
    op.add_column('poi_user_config', sa.Column('sensitivity', sa.Integer(), nullable=True), schema='customer')
    op.drop_constraint('poi_user_config_group_fkey', 'poi_user_config', schema='customer', type_='foreignkey')
    customer_poi_user_config_postgres_insert = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_insert)

    customer_poi_user_config_postgres_references = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_references)

    customer_poi_user_config_postgres_select = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_select)

    customer_poi_user_config_postgres_update = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_update)

    customer_poi_user_config_postgres_delete = PGGrantTable(schema='customer', table='poi_user_config', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_delete)

    customer_poi_user_config_postgres_truncate = PGGrantTable(schema='customer', table='poi_user_config', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_truncate)

    customer_poi_user_config_postgres_trigger = PGGrantTable(schema='customer', table='poi_user_config', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.drop_entity(customer_poi_user_config_postgres_trigger)

    public_distinct_intersection_existing_network_postgres_insert = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_insert)

    public_distinct_intersection_existing_network_postgres_references = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_references)

    public_distinct_intersection_existing_network_postgres_select = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_select)

    public_distinct_intersection_existing_network_postgres_update = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_update)

    public_distinct_intersection_existing_network_postgres_delete = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_delete)

    public_distinct_intersection_existing_network_postgres_truncate = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_truncate)

    public_distinct_intersection_existing_network_postgres_trigger = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.drop_entity(public_distinct_intersection_existing_network_postgres_trigger)

    basic_poi_default_config_postgres_insert = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_insert)

    basic_poi_default_config_postgres_references = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_references)

    basic_poi_default_config_postgres_select = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_select)

    basic_poi_default_config_postgres_update = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_update)

    basic_poi_group_postgres_insert = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_insert)

    basic_poi_group_postgres_references = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_references)

    basic_poi_group_postgres_select = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_select)

    basic_poi_group_postgres_update = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_update)

    basic_poi_study_area_config_postgres_insert = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_insert)

    basic_poi_study_area_config_postgres_references = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_references)

    basic_poi_study_area_config_postgres_select = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_select)

    basic_poi_study_area_config_postgres_update = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_update)

    basic_poi_group_postgres_delete = PGGrantTable(schema='basic', table='poi_group', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_delete)

    basic_poi_group_postgres_truncate = PGGrantTable(schema='basic', table='poi_group', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_truncate)

    basic_poi_group_postgres_trigger = PGGrantTable(schema='basic', table='poi_group', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.drop_entity(basic_poi_group_postgres_trigger)

    basic_poi_default_config_postgres_delete = PGGrantTable(schema='basic', table='poi_default_config', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_delete)

    basic_poi_default_config_postgres_truncate = PGGrantTable(schema='basic', table='poi_default_config', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_truncate)

    basic_poi_default_config_postgres_trigger = PGGrantTable(schema='basic', table='poi_default_config', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.drop_entity(basic_poi_default_config_postgres_trigger)

    basic_poi_study_area_config_postgres_delete = PGGrantTable(schema='basic', table='poi_study_area_config', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_delete)

    basic_poi_study_area_config_postgres_truncate = PGGrantTable(schema='basic', table='poi_study_area_config', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_truncate)

    basic_poi_study_area_config_postgres_trigger = PGGrantTable(schema='basic', table='poi_study_area_config', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.drop_entity(basic_poi_study_area_config_postgres_trigger)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    basic_poi_study_area_config_postgres_trigger = PGGrantTable(schema='basic', table='poi_study_area_config', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_trigger)

    basic_poi_study_area_config_postgres_truncate = PGGrantTable(schema='basic', table='poi_study_area_config', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_truncate)

    basic_poi_study_area_config_postgres_delete = PGGrantTable(schema='basic', table='poi_study_area_config', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_delete)

    basic_poi_default_config_postgres_trigger = PGGrantTable(schema='basic', table='poi_default_config', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_trigger)

    basic_poi_default_config_postgres_truncate = PGGrantTable(schema='basic', table='poi_default_config', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_truncate)

    basic_poi_default_config_postgres_delete = PGGrantTable(schema='basic', table='poi_default_config', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_delete)

    basic_poi_group_postgres_trigger = PGGrantTable(schema='basic', table='poi_group', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_trigger)

    basic_poi_group_postgres_truncate = PGGrantTable(schema='basic', table='poi_group', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_truncate)

    basic_poi_group_postgres_delete = PGGrantTable(schema='basic', table='poi_group', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_delete)

    basic_poi_study_area_config_postgres_update = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_update)

    basic_poi_study_area_config_postgres_select = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_select)

    basic_poi_study_area_config_postgres_references = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_references)

    basic_poi_study_area_config_postgres_insert = PGGrantTable(schema='basic', table='poi_study_area_config', columns=['category', 'color', 'group', 'icon', 'id', 'is_active', 'study_area_id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.create_entity(basic_poi_study_area_config_postgres_insert)

    basic_poi_group_postgres_update = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_update)

    basic_poi_group_postgres_select = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_select)

    basic_poi_group_postgres_references = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_references)

    basic_poi_group_postgres_insert = PGGrantTable(schema='basic', table='poi_group', columns=['group', 'id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.create_entity(basic_poi_group_postgres_insert)

    basic_poi_default_config_postgres_update = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_update)

    basic_poi_default_config_postgres_select = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_select)

    basic_poi_default_config_postgres_references = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_references)

    basic_poi_default_config_postgres_insert = PGGrantTable(schema='basic', table='poi_default_config', columns=['category', 'color', 'group', 'icon', 'id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.create_entity(basic_poi_default_config_postgres_insert)

    public_distinct_intersection_existing_network_postgres_trigger = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_trigger)

    public_distinct_intersection_existing_network_postgres_truncate = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_truncate)

    public_distinct_intersection_existing_network_postgres_delete = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_delete)

    public_distinct_intersection_existing_network_postgres_update = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_update)

    public_distinct_intersection_existing_network_postgres_select = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_select)

    public_distinct_intersection_existing_network_postgres_references = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_references)

    public_distinct_intersection_existing_network_postgres_insert = PGGrantTable(schema='public', table='distinct_intersection_existing_network', columns=['geom', 'id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.create_entity(public_distinct_intersection_existing_network_postgres_insert)

    customer_poi_user_config_postgres_trigger = PGGrantTable(schema='customer', table='poi_user_config', columns=[], role='postgres', grant='TRIGGER', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_trigger)

    customer_poi_user_config_postgres_truncate = PGGrantTable(schema='customer', table='poi_user_config', columns=[], role='postgres', grant='TRUNCATE', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_truncate)

    customer_poi_user_config_postgres_delete = PGGrantTable(schema='customer', table='poi_user_config', columns=[], role='postgres', grant='DELETE', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_delete)

    customer_poi_user_config_postgres_update = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='UPDATE', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_update)

    customer_poi_user_config_postgres_select = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='SELECT', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_select)

    customer_poi_user_config_postgres_references = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='REFERENCES', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_references)

    customer_poi_user_config_postgres_insert = PGGrantTable(schema='customer', table='poi_user_config', columns=['category', 'color', 'data_upload_id', 'group', 'icon', 'id', 'study_area_id', 'user_id'], role='postgres', grant='INSERT', with_grant_option=True)
    op.create_entity(customer_poi_user_config_postgres_insert)

    op.create_foreign_key('poi_user_config_group_fkey', 'poi_user_config', 'poi_group', ['group'], ['group'], source_schema='customer', referent_schema='basic')
    op.drop_column('poi_user_config', 'sensitivity', schema='customer')
    op.create_foreign_key('poi_study_area_config_group_fkey', 'poi_study_area_config', 'poi_group', ['group'], ['group'], source_schema='basic', referent_schema='basic')
    op.drop_column('poi_study_area_config', 'sensitivity', schema='basic')
    op.create_foreign_key('poi_default_config_group_fkey', 'poi_default_config', 'poi_group', ['group'], ['group'], source_schema='basic', referent_schema='basic')
    op.drop_column('poi_default_config', 'sensitivity', schema='basic')
    # ### end Alembic commands ###
