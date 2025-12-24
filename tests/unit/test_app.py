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

def test_not_found(client):
    """Test 404 for non-existent endpoint"""
    response = client.get('/api/nonexistent')
    assert response.status_code == 404

def test_index_response_structure(client):
    """Test root endpoint returns all expected fields with correct types"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'name' in data
    assert 'version' in data
    assert 'environment' in data
    assert 'status' in data
    assert 'timestamp' in data
    assert isinstance(data['name'], str)
    assert isinstance(data['version'], str)
    assert isinstance(data['environment'], str)
    assert data['status'] == 'running'
    # Validate timestamp is ISO format
    assert 'T' in data['timestamp'] or data['timestamp'].count('-') >= 2
