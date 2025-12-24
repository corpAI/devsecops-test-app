"""Integration tests for the test application"""

import pytest
import requests
import os
import time

BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:5000")

@pytest.mark.integration
def test_health_endpoint():
    """Test health endpoint in integration"""
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'

@pytest.mark.integration
def test_api_endpoints():
    """Test API endpoints"""
    # Test root
    response = requests.get(f"{BASE_URL}/", timeout=5)
    assert response.status_code == 200
    
    # Test data endpoint
    response = requests.get(f"{BASE_URL}/api/data", timeout=5)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
