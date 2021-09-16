from ..extractors.json_ld import JSONLDExtractor
from ..strategies import (
    json_ld_get_normalized_exchange_locations,
    json_ld_get_normalized_exchange_units,
    json_ld_get_activities_list_from_rawdata,
    json_ld_add_activity_unit,
    json_ld_rename_metadata_fields,
    add_database_name,
    link_iterable_by_fields,
    link_technosphere_by_activity_hash,
    normalize_units,
    strip_biosphere_exc_locations,
)
from .base_lci import LCIImporter
from bw2data import Database, config


class JSONLDImporter(LCIImporter):
    """Importer for the `OLCD JSON-LD data format <https://github.com/GreenDelta/olca-schema>`__.

    See `discussion with linked issues here <https://github.com/brightway-lca/brightway2-io/issues/15>`__.

    """

    format = "OLCA JSON-LD"
    extractor = JSONLDExtractor

    def __init__(self, dirpath):
        self.strategies = [
            json_ld_get_normalized_exchange_locations,
            json_ld_get_normalized_exchange_units,
            json_ld_get_activities_list_from_rawdata,
            json_ld_add_activity_unit,
            json_ld_rename_metadata_fields,
        ]
        self.data = self.extractor.extract(dirpath)
