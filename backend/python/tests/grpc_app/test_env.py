from grpc_app.env import VERSION


def test_version():
    assert VERSION == '0.1.0'
