from azure.storage.fileshare import ShareFileClient
import requests
import datetime
import hashlib
import hmac
import base64
import json  # Import json module

workspace_id = "8a20bd50-9ef0-4b15-a009-8c19ff1a099b"
shared_key = "ZkWB2Kv2aLLHROrMvk3TVZPxhx+M6G57FFNdzxkuOQ/w5dPFDh/ssiBhl66EQAQSYSWJN4CnO40T8n3w+jG89Q=="
log_type = "custom_logs_from_filesahre_CL"  # Custom log name (suffix _CL is required)
connection_string = "DefaultEndpointsProtocol=https;AccountName=webappaccount12365;AccountKey=cjeh0dwZzESyA4F1OT/3eN3kHO1Dgvamop5e6YXSb70uvQlwVVzsVB4kCjdquJRQv2KDYXuHnNNX+AStQOEHrw==;EndpointSuffix=core.windows.net"

file_client = ShareFileClient.from_connection_string(
    conn_str=connection_string,
    share_name="<filesharemount>",
    file_path="InvestProAzureWorker-Issues.txt"
)

data = file_client.download_file().readall().decode('utf-8')

# Parse the file data into log entries
log_entries = [
    {
        "TimeGenerated": "2023-10-01T12:00:00Z",
        "LogEntry": "Sample log line 1"
    },
    {
        "TimeGenerated": "2023-10-01T12:01:00Z",
        "LogEntry": "Sample log line 2"
    }
]

timestamp = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
content = json.dumps(log_entries)
content_length = len(content)
signature = f"POST\n{content_length}\napplication/json\nx-ms-date:{timestamp}\n/api/logs"
encoded_signature = base64.b64encode(hmac.new(
    base64.b64decode(shared_key),
    msg=signature.encode('utf-8'),
    digestmod=hashlib.sha256
).digest()).decode()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"SharedKey {workspace_id}:{encoded_signature}",
    "x-ms-date": timestamp
}

response = requests.post(
    f"https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01",
    headers=headers,
    data=content
)

print(response.status_code)
print(response.text)
