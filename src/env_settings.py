from pydantic_settings import BaseSettings, SettingsConfigDict

class AzureSettings(BaseSettings):
    azure_client_id:str
    azure_tenant_id:str
    azure_client_secret:str
    azure_subscription_id:str

    model_config = SettingsConfigDict(
        env_file="D:/azure-automation/.env",
        env_file_encoding = "utf-8"
    )
