import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response_new_user = post_new_user(data.user_body)


def get_headers_with_token():
    new_user_response = post_new_user(data.user_body)
    headers_for_kit = data.headers.copy()
    headers_for_kit["Authorization"] = "Bearer " + new_user_response.json()["authToken"]
    return headers_for_kit


new_headers = get_headers_with_token()


def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=new_headers)


response_new_kit = post_new_client_kit(data.kit_body)

print(response_new_kit.status_code)
print(response_new_kit.text)
