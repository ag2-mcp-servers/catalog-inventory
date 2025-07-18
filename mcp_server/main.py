# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T08:55:51+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, HTTPBasic
from pydantic import conint, constr

from models import (
    AppliedInventoriesParametersServicePlan,
    ErrorNotFound,
    Filter,
    GraphQLRequest,
    GraphQLResponse,
    OrderParametersServiceOffering,
    ServiceCredential,
    ServiceCredentialsCollection,
    ServiceCredentialType,
    ServiceCredentialTypesCollection,
    ServiceInstance,
    ServiceInstancesCollection,
    ServiceInventoriesCollection,
    ServiceInventoriesIdTagPostRequest,
    ServiceInventoriesIdTagPostResponse,
    ServiceInventoriesIdUntagPostRequest,
    ServiceInventory,
    ServiceOffering,
    ServiceOfferingNode,
    ServiceOfferingNodesCollection,
    ServiceOfferingsCollection,
    ServiceOfferingsIdAppliedInventoriesTagsPostResponse,
    ServiceOfferingsIdOrderPostResponse,
    ServicePlan,
    ServicePlansCollection,
    SortBy,
    Source,
    SourcesCollection,
    TagsCollection,
    Task,
    TasksCollection,
)
from models.Openapi import JsonGetResponse

app = MCPProxy(
    contact={'email': 'support@redhat.com'},
    description='Catalog Inventory',
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    title='Catalog Inventory',
    version='1.0.0',
    servers=[
        {
            'description': 'Production Server',
            'url': 'https://cloud.redhat.com/{basePath}',
            'variables': {'basePath': {'default': '/api/catalog-inventory/v1.0'}},
        },
        {
            'description': 'Development Server',
            'url': 'http://localhost:{port}/{basePath}',
            'variables': {
                'basePath': {'default': '/api/catalog-inventory/v1.0'},
                'port': {'default': '3000'},
            },
        },
    ],
)


@app.post(
    '/graphql',
    description=""" Performs a GraphQL Query """,
    tags=['graphql_operations'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def post_graph_q_l(body: GraphQLRequest):
    """
    Perform a GraphQL Query
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/openapi.json',
    tags=['service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def get_documentation():
    """
    Return this API document in JSON format
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_credential_types',
    description=""" Returns an array of ServiceCredentialType objects """,
    tags=['service_credentials_management', 'graphql_operations'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_credential_types(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServiceCredentialTypes
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_credential_types/{id}',
    description=""" Returns a ServiceCredentialType object """,
    tags=['service_credentials_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_credential_type(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServiceCredentialType
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_credentials',
    description=""" Returns an array of ServiceCredential objects """,
    tags=['service_credentials_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_credentials(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServiceCredentials
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_credentials/{id}',
    description=""" Returns a ServiceCredential object """,
    tags=['service_credentials_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_credential(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServiceCredential
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_instances',
    description=""" Returns an array of ServiceInstance objects """,
    tags=['service_instance_management', 'service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_instances(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServiceInstances
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_instances/{id}',
    description=""" Returns a ServiceInstance object """,
    tags=['service_instance_management', 'service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_instance(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServiceInstance
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_inventories',
    description=""" Returns an array of ServiceInventory objects """,
    tags=['service_inventory_management', 'graphql_operations'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_inventories(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServiceInventories
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_inventories/{id}',
    description=""" Returns a ServiceInventory object """,
    tags=['service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_inventory(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServiceInventory
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/service_inventories/{id}/tag',
    description=""" Tags a ServiceInventory object """,
    tags=['service_inventory_management', 'tag_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def tag_service_inventory(
    id: constr(pattern=r'^\d+$'), body: ServiceInventoriesIdTagPostRequest = ...
):
    """
    Tag a ServiceInventory
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_inventories/{id}/tags',
    description=""" Returns an array of Tag objects """,
    tags=['service_inventory_management', 'tag_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_inventory_tags(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List Tags for ServiceInventory
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/service_inventories/{id}/untag',
    description=""" Untags a ServiceInventory object """,
    tags=['service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def untag_service_inventory(
    id: constr(pattern=r'^\d+$'), body: ServiceInventoriesIdUntagPostRequest = ...
):
    """
    Untag a ServiceInventory
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offering_nodes',
    description=""" Returns an array of ServiceOfferingNode objects """,
    tags=['service_offering_management', 'service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_offering_nodes(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServiceOfferingNodes
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offering_nodes/{id}',
    description=""" Returns a ServiceOfferingNode object """,
    tags=['service_offering_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_offering_node(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServiceOfferingNode
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offerings',
    description=""" Returns an array of ServiceOffering objects """,
    tags=['service_offering_management', 'service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_offerings(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServiceOfferings
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offerings/{id}',
    description=""" Returns a ServiceOffering object """,
    tags=['service_offering_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_offering(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServiceOffering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/service_offerings/{id}/applied_inventories_tags',
    description=""" Returns an array of inventories tags """,
    tags=[
        'service_inventory_management',
        'service_offering_management',
        'tag_management',
    ],
    security=[
        HTTPBasic(name="None"),
    ],
)
def applied_inventories_tags_for_service_offering(
    id: constr(pattern=r'^\d+$'), body: AppliedInventoriesParametersServicePlan = ...
):
    """
    Invokes computing of ServiceInventories tags for given ServiceOffering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/service_offerings/{id}/order',
    description=""" Returns a Task id """,
    tags=['service_offering_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def order_service_offering(
    id: constr(pattern=r'^\d+$'), body: OrderParametersServiceOffering = ...
):
    """
    Order an existing ServiceOffering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offerings/{id}/service_instances',
    description=""" Returns an array of ServiceInstance objects """,
    tags=['service_instance_management', 'service_offering_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_offering_service_instances(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServiceInstances for ServiceOffering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offerings/{id}/service_offering_nodes',
    description=""" Returns an array of ServiceOfferingNode objects """,
    tags=['service_offering_management', 'service_inventory_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_offering_service_offering_nodes(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServiceOfferingNodes for ServiceOffering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_offerings/{id}/service_plans',
    description=""" Returns an array of ServicePlan objects """,
    tags=['service_plan_management', 'service_offering_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_offering_service_plans(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServicePlans for ServiceOffering
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_plans',
    description=""" Returns an array of ServicePlan objects """,
    tags=[
        'service_plan_management',
        'service_offering_management',
        'source_service_listing',
    ],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_service_plans(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List ServicePlans
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/service_plans/{id}',
    description=""" Returns a ServicePlan object """,
    tags=['service_plan_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_service_plan(id: constr(pattern=r'^\d+$')):
    """
    Show an existing ServicePlan
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources',
    description=""" Returns an array of Source objects """,
    tags=['source_management', 'source_service_listing'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_sources(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List Sources
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}',
    description=""" Returns a Source object """,
    tags=['source_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_source(id: constr(pattern=r'^\d+$')):
    """
    Show an existing Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/sources/{id}/incremental_refresh',
    description=""" Incremental Refresh a source object """,
    tags=['source_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def incremental_refresh_source(id: constr(pattern=r'^\d+$')):
    """
    Incremental Refresh an existing Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/sources/{id}/refresh',
    description=""" Refresh a source object """,
    tags=['source_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def refresh_source(id: constr(pattern=r'^\d+$')):
    """
    Refresh an existing Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}/service_instances',
    description=""" Returns an array of ServiceInstance objects """,
    tags=['service_instance_management', 'source_service_listing'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_source_service_instances(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServiceInstances for Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}/service_inventories',
    description=""" Returns an array of ServiceInventory objects """,
    tags=[
        'service_inventory_management',
        'source_management',
        'source_service_listing',
    ],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_source_service_inventories(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServiceInventories for Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}/service_offering_nodes',
    description=""" Returns an array of ServiceOfferingNode objects """,
    tags=['service_offering_management', 'source_management', 'source_service_listing'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_source_service_offering_nodes(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServiceOfferingNodes for Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}/service_offerings',
    description=""" Returns an array of ServiceOffering objects """,
    tags=['service_offering_management', 'source_service_listing'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_source_service_offerings(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServiceOfferings for Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}/service_plans',
    description=""" Returns an array of ServicePlan objects """,
    tags=['service_plan_management', 'source_service_listing'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_source_service_plans(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List ServicePlans for Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sources/{id}/tasks',
    description=""" Returns an array of Task objects """,
    tags=['task_management', 'source_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_source_tasks(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
    id: constr(pattern=r'^\d+$') = ...,
):
    """
    List Tasks for Source
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tags',
    description=""" Returns an array of Tag objects """,
    tags=['tag_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_tags(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List Tags
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tasks',
    description=""" Returns an array of Task objects """,
    tags=['task_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def list_tasks(
    limit: Optional[conint(ge=1, le=1000)] = 100,
    offset: Optional[conint(ge=0)] = 0,
    filter: Optional[Filter] = None,
    sort_by: Optional[SortBy] = None,
):
    """
    List Tasks
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tasks/{id}',
    description=""" Returns a Task object """,
    tags=['task_management', 'graphql_operations'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def show_task(
    id: constr(pattern=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'),
):
    """
    Show an existing Task
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/tasks/{id}',
    description=""" Updates a Task object """,
    tags=['task_management'],
    security=[
        HTTPBasic(name="None"),
    ],
)
def update_task(
    id: constr(pattern=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'),
    body: Task = ...,
):
    """
    Update an existing Task
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
