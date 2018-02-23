# -*- coding: utf-8 -*-

"""
A convenience script for generating an interactive test environment.
"""

from __future__ import absolute_import
import nipyapi

# Note that this is the URI for NiFi to connect to Registry
# Which may be different from your localhost connection if using Docker
# Docker is likely to be http://<docker name for registry>:18080
_rc_endpoint = 'http://registry:18080'

_basename = "nipyapi_console"
_pg0 = _basename + '_process_group_0'
_proc0 = _basename + '_processor_0'
_rc0 = _basename + '_reg_client_0'
_b0 = _basename + '_bucket_0'
_b1 = _basename + '_bucket_1'
_vf0 = _basename + '_ver_flow_0'
_vf1 = _basename + '_ver_flow_1'

__all__ = ['process_group_0', 'processor_0', 'reg_client_0', 'bucket_0',
           'bucket_1', 'ver_flow_info_0', 'ver_flow_0', 'ver_flow_snapshot_0',
           'ver_flow_1', 'ver_flow_snapshot_1', 'ver_flow_json_0',
           'ver_flow_yaml_0', 'ver_flow_raw_0']

# recreate or create a process group
process_group_0 = nipyapi.canvas.get_process_group(_pg0)
if process_group_0 is not None:
    nipyapi.canvas.delete_process_group(
        process_group_0,
        force=True,
        refresh=True
    )
process_group_0 = nipyapi.canvas.create_process_group(
    nipyapi.canvas.get_process_group(nipyapi.canvas.get_root_pg_id(), 'id'),
    _pg0,
    location=(400.0, 400.0)
)

# Get or create a processor in the above PG
processor_0 = nipyapi.canvas.get_processor(_proc0)
if processor_0 is not None:
    nipyapi.canvas.delete_processor(process_group_0, True)
processor_0 = nipyapi.canvas.create_processor(
    parent_pg=process_group_0,
    processor=nipyapi.canvas.get_processor_type('GenerateFlowFile'),
    location=(400.0, 400.0),
    name=_proc0,
    config=nipyapi.nifi.ProcessorConfigDTO(
        scheduling_period='1s',
        auto_terminated_relationships=['success']
    )
)

# get or create a registry client
try:
    reg_client_0 = nipyapi.versioning.create_registry_client(
        name=_rc0,
        uri=_rc_endpoint,
        description='NiPyApi Test'
    )
except ValueError:
    reg_client_0 = nipyapi.versioning.get_registry_client(_rc0)

# recreate or create two buckets
bucket_0 = nipyapi.versioning.get_registry_bucket(_b0)
if bucket_0 is not None:
    nipyapi.versioning.delete_registry_bucket(bucket_0)
bucket_0 = nipyapi.versioning.create_registry_bucket(_b0)
bucket_1 = nipyapi.versioning.get_registry_bucket(_b1)
if bucket_1 is not None:
    nipyapi.versioning.delete_registry_bucket(bucket_1)
bucket_1 = nipyapi.versioning.create_registry_bucket(_b1)

# Save the PG + Proc to the first bucket as a new version
ver_flow_info_0 = nipyapi.versioning.save_flow_ver(
    process_group=process_group_0,
    registry_client=reg_client_0,
    bucket=bucket_0,
    flow_name=_vf0,
    desc='A Versioned Flow',
    comment='A Versioned Flow'
)
ver_flow_0 = nipyapi.versioning.get_flow_in_bucket(
    bucket_0.identifier,
    ver_flow_info_0.version_control_information.flow_id,
    'id'
)
ver_flow_snapshot_0 = nipyapi.versioning.get_latest_flow_ver(
    bucket_0.identifier, ver_flow_0.identifier
)

# Create a flow version stub the second bucket
ver_flow_1 = nipyapi.versioning.create_flow(
    bucket_id=bucket_1.identifier,
    flow_name=_vf1,
    flow_desc='A cloned Versioned NiFi-Registry Flow'
)

# Clone the versioned flow into the new stub flow in the
ver_flow_snapshot_1 = nipyapi.versioning.create_flow_version(
    flow=ver_flow_1,
    flow_snapshot=ver_flow_snapshot_0
)

# # Export the Flow to Json/Yaml/raw
ver_flow_raw_0 = nipyapi.versioning.get_flow_version(
    bucket_0.identifier, ver_flow_0.identifier, export=True
)
ver_flow_json_0 = nipyapi.versioning.export_flow_version(
    bucket_0.identifier, ver_flow_0.identifier, mode='json'
)
ver_flow_yaml_0 = nipyapi.versioning.export_flow_version(
    bucket_0.identifier, ver_flow_0.identifier, mode='yaml'
)
