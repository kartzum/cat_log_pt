class Provider:
    def __init__(self, identifier: str, name: str):
        self.identifier = identifier
        self.name = name


class CatalogSchemeOperation:
    def __init__(self, identifier: str, name: str, scheme_id: str, catalog_id: str):
        self.identifier = identifier
        self.name = name
        self.scheme_id = scheme_id
        self.catalog_id = catalog_id


class CatalogSchemeOperationInstance:
    def __init__(self, identifier: str, name: str, operation_scheme_id: str, catalog_id: str):
        self.identifier = identifier
        self.name = name
        self.operation_scheme_id = operation_scheme_id
        self.catalog_id = catalog_id
        self.is_running = False
        self.is_complete = False


class CatalogScheme:
    def __init__(self, identifier: str, name: str):
        self.identifier = identifier
        self.name = name


class Catalog:
    def __init__(self, identifier: str, name: str, provider_id: str, scheme_id: str):
        self.identifier = identifier
        self.name = name
        self.provider_id = provider_id
        self.scheme_id = scheme_id


class CatalogOperationInstanceResult:
    def __init__(self, identifier: str, operation_instance_id: str, catalog_id: str, result: object):
        self.identifier = identifier
        self.operation_instance_id = operation_instance_id
        self.catalog_id = catalog_id
        self.result = result


class AppData:
    def __init__(
            self,
            providers,
            catalogs,
            catalog_schemes,
            catalog_scheme_operations,
            catalog_scheme_operation_instances,
            catalog_results
    ):
        self.providers = providers
        self.catalogs = catalogs
        self.catalog_schemes = catalog_schemes
        self.catalog_scheme_operations = catalog_scheme_operations
        self.catalog_scheme_operation_instances = catalog_scheme_operation_instances
        self.catalog_results = catalog_results


skProvider = Provider(identifier="d119bc73-7125-4ffe-8ca6-f48c2ef58242", name="SK")

skNewCatalogScheme = CatalogScheme(identifier="8182b5fe-f963-485e-8b62-0a008b2499aa", name="SK_new_scheme")

skNewCatalog = Catalog(
    identifier="3d8dd856-363d-4dc0-8a3c-614a7ac0af99",
    name="SK_new_catalog",
    provider_id="d119bc73-7125-4ffe-8ca6-f48c2ef58242",
    scheme_id="8182b5fe-f963-485e-8b62-0a008b2499aa"
)

skNewCatalogSchemeOperation = CatalogSchemeOperation(
    identifier="bb8c681b-fc5f-49d3-817d-7d5f50e811e0",
    name="SK_load_new",
    scheme_id="8182b5fe-f963-485e-8b62-0a008b2499aa",
    catalog_id="3d8dd856-363d-4dc0-8a3c-614a7ac0af99",
)

data = AppData(
    providers={skProvider.identifier: skProvider},
    catalogs={skNewCatalog.identifier: skNewCatalog},
    catalog_schemes={skNewCatalogScheme.identifier: skNewCatalogScheme},
    catalog_scheme_operations={skNewCatalogSchemeOperation.identifier: skNewCatalogSchemeOperation},
    catalog_scheme_operation_instances={},
    catalog_results={},
)


async def app_data() -> AppData:
    return data
