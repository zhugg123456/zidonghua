import pytest

from JinRongZongHe.baw.DbOp import DbOp
from JinRongZongHe.baw.Member import Member
from JinRongZongHe.caw.Assert import Assert
from JinRongZongHe.caw.DataRead import DataRead


@pytest.fixture(params=DataRead().read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param


# 登录的测试逻辑
def test_login(url, base_requests, register, login_data):
    r = Member().login(url, base_requests, login_data['data'])
    Assert().equal(login_data['expect'], r.json(), "msg,status,code")
