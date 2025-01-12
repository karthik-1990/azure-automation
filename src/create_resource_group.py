from azure.core.exceptions import ResourceNotFoundError
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

from env_settings import AzureSettings

def main():
    config=AzureSettings()
    credential = ClientSecretCredential(
        tenant_id=config.azure_tenant_id,
        client_id=config.azure_client_id,
        client_secret=config.azure_client_secret
    )
    resource_client = ResourceManagementClient(credential, config.azure_subscription_id)
    resource_group_name = "azr-appdev-rg-dev"
    location = "centralindia"
    try:
        rg_result = resource_client.resource_groups.get(resource_group_name)
        print(f"resource group '{rg_result.name}' already exists in location '{rg_result.location}'")
    except ResourceNotFoundError:
        print(f"Resource group {resource_group_name} does not exists and hence creating a new one...")

        rg_result = resource_client.resource_groups.create_or_update(
            resource_group_name,
            {"location":location}
        )
        print(f"Resource group'{rg_result.name}' created in location '{rg_result.location}'")

if __name__ == "__main__":
    main()