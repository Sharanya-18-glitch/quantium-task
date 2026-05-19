from app import app

def test_header_present():
    assert app is not None

def test_layout_present():
    assert app.layout is not None

def test_graph_present():
    layout_str = str(app.layout)
    assert "sales-chart" in layout_str