import json

import httpx

BASE_URL = "dummy base url"


async def get_notifications() -> httpx.Response:
    endpoint = f"https://{BASE_URL}/api/mojo/open/notifications/10"

    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(endpoint)
        # print(response.json())
        return response


async def post_notification() -> httpx.Response:
    endpoint = f"https://{BASE_URL}/api/mojo/new/notification"

    payload = {"TargetId": 14080338, "EventType": "EntityUpdated", "TargetDefinition": "M.Asset", "Data": {"Culture": "(Default)", "Name": None, "Definition": "M.Asset", "PropertyChanges": [], "RelationChanges": [
        {"Relation": "MediaMatrixToAsset", "Role": "Child", "Definition": "M.Asset", "Values": {"Added": [{"Id": 32754, "Name": None}], "Removed": []}}]}, "TimeStamp": "2023-09-22T13:30:59.869Z"}

    json_str = json.dumps(payload)

    headers = {'Content-Type': 'application/json'}
    async with httpx.AsyncClient(verify=False, headers=headers) as client:
        response = await client.post(endpoint, data=json_str)
        # print(response)
        return response


async def update_notifications() -> httpx.Response:
    endpoint = f"https://{BASE_URL}/api/mojo/open/notifications"

    payload = ["650c0507673f5bfb2faf772f",
               "650dafda0843c75a4440444e", "650db07a0843c75a4440444f"]

    json_str = json.dumps(payload)

    headers = {'Content-Type': 'application/json'}
    async with httpx.AsyncClient(verify=False, headers=headers) as client:
        response = await client.patch(endpoint, data=json_str)
        # print(response)
        return response


async def delete_notifications() -> httpx.Response:
    endpoint = f"https://{BASE_URL}/api/mojo/old/notifications?days=3"

    headers = {'Content-Type': 'application/json'}
    async with httpx.AsyncClient(verify=False, headers=headers) as client:
        response = await client.delete(endpoint)
        # print(response)
        return response
