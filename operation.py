import uuid

from model import AppData, CatalogSchemeOperationInstance, CatalogSchemeOperation

from sk_operation import SkLoadNewOperation


def run_operation(scheme_operation: CatalogSchemeOperation, application_data: AppData):
    if "SK_load_new" in scheme_operation.name:
        instance = CatalogSchemeOperationInstance(
            str(uuid.uuid1()),
            scheme_operation.name,
            scheme_operation.identifier,
            scheme_operation.catalog_id,
        )
        application_data.catalog_scheme_operation_instances[instance.identifier] = instance
        SkLoadNewOperation(instance, application_data).run()
