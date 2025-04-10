class TestOrderList:
    def test_get_order_list(self, order_methods):
        response = order_methods.get_order_list()
        assert response.status_code == 200
        assert 'orders' in response.text
