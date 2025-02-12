from azure.storage.fileshare import ShareFileClient

connection_string = "<DefaultEndpointsProtocol=https;AccountName=webappaccount12365;AccountKey=cjeh0dwZzESyA4F1OT/3eN3kHO1Dgvamop5e6YXSb70uvQlwVVzsVB4kCjdquJRQv2KDYXuHnNNX+AStQOEHrw==;EndpointSuffix=core.windows.net>"
file_client = ShareFileClient.from_connection_string(
    conn_str=connection_string,
    share_name="<filesharemount>",
    file_path="InvestProAzureWorker-Issues.txt"
)
data = file_client.download_file().readall().decode('utf-8')
