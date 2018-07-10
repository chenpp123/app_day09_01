import allure


class Test_aa:

    def test_abc(self):
        # 添加描述
        allure.attach("描述","描述内容")

        with open("./Screen/test.png","rb") as f:
            allure.attach("屏幕截图",f.read(),allure.attach_type.PNG)
            
        assert 0,"hahahahha"

