def pytest_tavern_beta_after_every_response(expected, response):
    print("Got response:", response.json())
