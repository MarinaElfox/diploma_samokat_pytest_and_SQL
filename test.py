# Марина Любимова, 9-я когорта. Финальный протек. Инженер по тестированию плюс.
import sender_stand

def test_status_code_get_order_by_track():
    assert sender_stand.response_order.status_code == 200