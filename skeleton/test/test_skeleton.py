import skeleton


class TestDummy:
    def test_getname(self):
        assert 'I am a walking skeleton!' == skeleton.greet()
