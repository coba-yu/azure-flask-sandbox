# backend

## For developers

### Setup

#### Azure CLI

install

```shell
brew update && brew install azure-cli
```

setup

```shell
az login
az account set --subscription <subscription_id>
```

## References

- [Install Azure CLI ](https://learn.microsoft.com/ja-jp/cli/azure/install-azure-cli)
- Flask アプリをコンテナーとして Azure App Service にデプロイするチュートリアル
  - https://learn.microsoft.com/ja-jp/azure/developer/python/tutorial-containerize-simple-web-app-for-app-service
  - https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart
