from decimal import Decimal

# 尝试 decimal 数据类型运算，是否有浮点误差
a, b = Decimal('29337.56'), Decimal('29337.56')
print(str((b - a) / a))
