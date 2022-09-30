
def test_healthcheck_response_should_be_ok(client):
  response = client.get("/healthcheck")
  body = response.json()

  assert response.status_code == 200
  assert body["status"] == "OK"
