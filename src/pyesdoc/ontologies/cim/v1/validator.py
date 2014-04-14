# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.validator.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of validators over the cim 1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-04-14 15:44:38.720092.

"""

# Module imports.
from validator_for_activity_package import *
from validator_for_data_package import *
from validator_for_grids_package import *
from validator_for_misc_package import *
from validator_for_quality_package import *
from validator_for_shared_package import *
from validator_for_software_package import *

import validator_for_activity_package as activity
import validator_for_data_package as data
import validator_for_grids_package as grids
import validator_for_misc_package as misc
import validator_for_quality_package as quality
import validator_for_shared_package as shared
import validator_for_software_package as software



# Module exports.
__all__ = [
    'supported',
    'validate_activity',
    'validate_boundary_condition',
    'validate_conformance',
    'validate_downscaling_simulation',
    'validate_ensemble',
    'validate_ensemble_member',
    'validate_experiment',
    'validate_experiment_relationship',
    'validate_experiment_relationship_target',
    'validate_initial_condition',
    'validate_lateral_boundary_condition',
    'validate_measurement_campaign',
    'validate_numerical_activity',
    'validate_numerical_experiment',
    'validate_numerical_requirement',
    'validate_numerical_requirement_option',
    'validate_output_requirement',
    'validate_physical_modification',
    'validate_simulation',
    'validate_simulation_composite',
    'validate_simulation_relationship',
    'validate_simulation_relationship_target',
    'validate_simulation_run',
    'validate_spatio_temporal_constraint',
    'validate_data_content',
    'validate_data_distribution',
    'validate_data_extent',
    'validate_data_extent_geographical',
    'validate_data_extent_temporal',
    'validate_data_extent_time_interval',
    'validate_data_hierarchy_level',
    'validate_data_object',
    'validate_data_property',
    'validate_data_restriction',
    'validate_data_storage',
    'validate_data_storage_db',
    'validate_data_storage_file',
    'validate_data_storage_ip',
    'validate_data_topic',
    'validate_coordinate_list',
    'validate_grid_extent',
    'validate_grid_mosaic',
    'validate_grid_property',
    'validate_grid_spec',
    'validate_grid_tile',
    'validate_grid_tile_resolution_type',
    'validate_vertical_coordinate_list',
    'validate_cim_quality',
    'validate_evaluation',
    'validate_measure',
    'validate_report',
    'validate_calendar',
    'validate_change',
    'validate_change_property',
    'validate_citation',
    'validate_closed_date_range',
    'validate_compiler',
    'validate_daily_360',
    'validate_data_source',
    'validate_date_range',
    'validate_doc_genealogy',
    'validate_doc_meta_info',
    'validate_doc_reference',
    'validate_doc_relationship',
    'validate_doc_relationship_target',
    'validate_license',
    'validate_machine',
    'validate_machine_compiler_unit',
    'validate_open_date_range',
    'validate_perpetual_period',
    'validate_platform',
    'validate_property',
    'validate_real_calendar',
    'validate_relationship',
    'validate_responsible_party',
    'validate_responsible_party_contact_info',
    'validate_standard',
    'validate_standard_name',
    'validate_component',
    'validate_component_language',
    'validate_component_language_property',
    'validate_component_property',
    'validate_composition',
    'validate_connection',
    'validate_connection_endpoint',
    'validate_connection_property',
    'validate_coupling',
    'validate_coupling_endpoint',
    'validate_coupling_property',
    'validate_deployment',
    'validate_entry_point',
    'validate_model_component',
    'validate_parallelisation',
    'validate_processor_component',
    'validate_rank',
    'validate_spatial_regridding',
    'validate_spatial_regridding_property',
    'validate_spatial_regridding_user_method',
    'validate_statistical_model_component',
    'validate_time_lag',
    'validate_time_transformation',
    'validate_timing',
    'validate_document_set',
]



# Supported validators.
supported = (
    activity.validate_activity,
    activity.validate_boundary_condition,
    activity.validate_conformance,
    activity.validate_downscaling_simulation,
    activity.validate_ensemble,
    activity.validate_ensemble_member,
    activity.validate_experiment,
    activity.validate_experiment_relationship,
    activity.validate_experiment_relationship_target,
    activity.validate_initial_condition,
    activity.validate_lateral_boundary_condition,
    activity.validate_measurement_campaign,
    activity.validate_numerical_activity,
    activity.validate_numerical_experiment,
    activity.validate_numerical_requirement,
    activity.validate_numerical_requirement_option,
    activity.validate_output_requirement,
    activity.validate_physical_modification,
    activity.validate_simulation,
    activity.validate_simulation_composite,
    activity.validate_simulation_relationship,
    activity.validate_simulation_relationship_target,
    activity.validate_simulation_run,
    activity.validate_spatio_temporal_constraint,
    data.validate_data_content,
    data.validate_data_distribution,
    data.validate_data_extent,
    data.validate_data_extent_geographical,
    data.validate_data_extent_temporal,
    data.validate_data_extent_time_interval,
    data.validate_data_hierarchy_level,
    data.validate_data_object,
    data.validate_data_property,
    data.validate_data_restriction,
    data.validate_data_storage,
    data.validate_data_storage_db,
    data.validate_data_storage_file,
    data.validate_data_storage_ip,
    data.validate_data_topic,
    grids.validate_coordinate_list,
    grids.validate_grid_extent,
    grids.validate_grid_mosaic,
    grids.validate_grid_property,
    grids.validate_grid_spec,
    grids.validate_grid_tile,
    grids.validate_grid_tile_resolution_type,
    grids.validate_vertical_coordinate_list,
    quality.validate_cim_quality,
    quality.validate_evaluation,
    quality.validate_measure,
    quality.validate_report,
    shared.validate_calendar,
    shared.validate_change,
    shared.validate_change_property,
    shared.validate_citation,
    shared.validate_closed_date_range,
    shared.validate_compiler,
    shared.validate_daily_360,
    shared.validate_data_source,
    shared.validate_date_range,
    shared.validate_doc_genealogy,
    shared.validate_doc_meta_info,
    shared.validate_doc_reference,
    shared.validate_doc_relationship,
    shared.validate_doc_relationship_target,
    shared.validate_license,
    shared.validate_machine,
    shared.validate_machine_compiler_unit,
    shared.validate_open_date_range,
    shared.validate_perpetual_period,
    shared.validate_platform,
    shared.validate_property,
    shared.validate_real_calendar,
    shared.validate_relationship,
    shared.validate_responsible_party,
    shared.validate_responsible_party_contact_info,
    shared.validate_standard,
    shared.validate_standard_name,
    software.validate_component,
    software.validate_component_language,
    software.validate_component_language_property,
    software.validate_component_property,
    software.validate_composition,
    software.validate_connection,
    software.validate_connection_endpoint,
    software.validate_connection_property,
    software.validate_coupling,
    software.validate_coupling_endpoint,
    software.validate_coupling_property,
    software.validate_deployment,
    software.validate_entry_point,
    software.validate_model_component,
    software.validate_parallelisation,
    software.validate_processor_component,
    software.validate_rank,
    software.validate_spatial_regridding,
    software.validate_spatial_regridding_property,
    software.validate_spatial_regridding_user_method,
    software.validate_statistical_model_component,
    software.validate_time_lag,
    software.validate_time_transformation,
    software.validate_timing,
    misc.validate_document_set,
)