"""Unit tests for the test application"""

import pytest
import os
from src.app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'
    assert 'version' in data

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_get_data(client):
    """Test data endpoint"""
    response = client.get('/api/data')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data

def test_version(client):
    """Test version endpoint"""
    response = client.get('/api/version')
    assert response.status_code == 200
    data = response.get_json()
    assert 'version' in data
