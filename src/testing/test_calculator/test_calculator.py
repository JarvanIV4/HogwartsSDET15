# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/11/25 21:29
"""
课后作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""

from src.testing.test_calculator import Calculator
import pytest


class TestCaluator:

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', [[1, 1, 2], [100, 1, 200], [0.1, 0.1, 0.2], [-1, -1, -2], [1, 0, 1], [0.1, 0.2, 0.3]],
                             ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case', 'smallnum_case'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b', [[1, 0], [100, 0], [-1, 0]])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 1], [100, 100, 1], [200, 100, 2], [5, 10, 0.5], [0.4, 0.1, 4]])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert expect == result
        # try:
        #     result = self.calc.div(a, b)
        # except ZeroDivisionError:
        #     print("除数为0")


