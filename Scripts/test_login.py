import pytest, sys, os
sys.path.append(os.getcwd())
from Page.login_page import Login_Page
from Page.setting_page import Setting_Page
from Page.Page import Page
from Base.init_driver import get_driver
from Base.read_data import Op_Data
def get_data():
    # 读取返回数据
    data_list = []
    data = Op_Data("data.yml").read_yaml().get("Login_data")
    for i in data:
        for o in i.keys():
            data_list.append((o,i.get(o).get("phone"),i.get(o).get("passwd"),
                              i.get(o).get("get_mess"),i.get(o).get("expect_message"),
                              i.get(o).get("tag")))
    return data_list
class Test_Login:

    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(get_driver())
        self.page_obj.get_login_page().click_my_btn()

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("case_num, username, passwd,get_mess,expect_message, tag", get_data())
    def test_login_page(self, case_num, username, passwd, get_mess, expect_message, tag):
        """
        :param username: 用户名
        :param passwd: 密码
        :param get_mess: toast传参
        :param expect_message: 预期toast消息
        :param tag: 1 标记登陆成功用例
        :return:
        """
        # 点击登陆注册
        self.page_obj.get_login_page().click_login_sign_btn()
        # 登陆操作
        self.page_obj.get_login_page().login_input_page(username, passwd)
        if tag:
            try:
                # 获取登陆成功toast
                suc_msg = self.page_obj.get_login_page().get_toast(get_mess)
                # 获取我的订单状态
                order_status = self.page_obj.get_login_page().if_my_order_status()
                # 退出登录
                self.page_obj.get_setting_page().logout_page()
                assert suc_msg == expect_message and order_status

            except Exception as e:
                # 关闭登陆信息输入页面
                self.page_obj.get_login_page().login_close_page()
                assert False
        else:
            try:
                # 获取登陆失败toast消息
                fail_msg = self.page_obj.get_login_page().get_toast(get_mess)
                if fail_msg:
                    assert fail_msg == expect_message
                else:
                    assert False
            finally:
                self.page_obj.get_login_page().login_close_page()


