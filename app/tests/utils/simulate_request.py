def simulate_request(
    client, endpoint: str, action: str = "GET", message_context: dict = {}
):
    if action == "GET":
        response = client.get(url=endpoint)
    elif action == "POST":
        response = client.post(url=endpoint, json=message_context)
    elif action == "PUT":
        response = client.put(url=endpoint, json=message_context)
    elif action == "DELETE":
        response = client.delete(url=endpoint)
    return response
