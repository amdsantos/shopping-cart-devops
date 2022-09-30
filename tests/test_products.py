
def test_get_products_should_return_empty_list(client):
  response = client.get("/products?skip=0&limit=100")
  body = response.json()

  assert response.status_code == 200
  assert body["data"]["products"] == []
