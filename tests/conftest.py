import asyncio
import pytest
from fastapi.testclient import TestClient
from api.app import app
from api.server.database import connect_db

@pytest.fixture
def client():
  client = TestClient(app)
  asyncio.run(connect_db())

  return client
