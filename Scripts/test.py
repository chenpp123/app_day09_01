import allure
import pytest

class Test_aa:

    def get_screen(self):
        with open("./Screen/test.png","rb") as f:
            allure.attach("屏幕截图",f.read(),allure.attach_type.PNG)

    def test_abc(self):
        # 添加描述
        allure.attach("描述","描述内容")

        assert 0,self.get_screen()

