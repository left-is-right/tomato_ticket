import pandas as pd
from decimal import *


def dataProcessServer(ori_data, output_file, weight_coe, price):

    status = 0
    try:
        ori_data = ori_data[['流水号', '磅单编号', '排队号', '车牌号', '车辆类型', '合同号', '经济人姓名', '农户姓名', '电话',
                             '身份证号', '地址', '货物名称', '毛重', '皮重', '带杂重', '扣杂率', '净重', '单价', '金额',
                             '登记时间', '重磅员', '回皮时间', '回皮员', '审核员', '质检员', '结算标志', '作废时间', '作废人',
                             '开户行代码', '开户行名称', '户名', '卡号', '确权证号', '承包合同', '付款方式', '低保户编号',
                             '备注', '未扣净重', '扣杂重']]
    except KeyError:
        try:
            ori_data = ori_data[['流水号', '毛重', '皮重', '净重', '单价', '金额']]
        except KeyError:
            status = 1
            return status

    mask = ori_data['流水号'].str.contains('^[0-9]*$')
    res_data = ori_data[mask]

    res_data['毛重'] = res_data['毛重'].apply(lambda x: Decimal(x))
    res_data['单价'] = price
    res_data['皮重'] = res_data['皮重'].apply(lambda x: Decimal(x))
    res_data['毛重'] = res_data['毛重'] * weight_coe
    res_data['净重'] = res_data['毛重'] - res_data['皮重']
    res_data['金额'] = res_data['单价'] * res_data['净重']

    res_data['金额'] = res_data['金额'].apply(lambda x: round(x, 0))
    # ori_data['金额（大写）'] = ori_data['金额（整）'].apply(lambda x: num_2_cn(str(x)))

    try:
        res_data.to_excel(output_file, index=False)
    except Exception as e:
        print(e)
        status = 2

    return status


def dataProcessKfServer(ori_data, output_file, weight_coe, price):

    status = 0
    try:
        ori_data.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
        ori_data = ori_data[['序号', '流水号', '车号', '农户姓名', '毛重', '毛重时间', '皮重', '净重', '扣量', '实重',
                             '单价', '金额', '皮重时间']]
    except KeyError:
        try:
            ori_data = ori_data[['序号', '毛重', '皮重', '净重', '单价', '金额']]
        except KeyError:
            status = 1
            return status

    ori_data.dropna(subset=['序号'], inplace=True)
    mask = ori_data['序号'].str.contains('^[0-9]*$')
    res_data = ori_data[mask]

    res_data['毛重'] = res_data['毛重'].apply(lambda x: Decimal(x))
    res_data['单价'] = price
    res_data['皮重'] = res_data['皮重'].apply(lambda x: Decimal(x))
    res_data['毛重'] = res_data['毛重'] * weight_coe
    res_data['净重'] = res_data['毛重'] - res_data['皮重']
    res_data['金额'] = res_data['单价'] * res_data['净重']

    res_data['金额'] = res_data['金额'].apply(lambda x: round(x, 0))

    try:
        res_data.to_excel(output_file, index=False)
    except Exception as e:
        print(e)
        status = 2

    return status


if __name__ == '__main__':
    input_file = 'D:/私人/数据处理/456.xlsx'
    output_file = 'D:/私人/数据处理/456-处理后.xlsx'
    weight_coe_var = '1.2'
    weight_coe = Decimal(weight_coe_var)
    print(weight_coe_var.isdigit())
    print('1'.isdigit())
    price_coe_var = '1.2'
    price_coe = Decimal(price_coe_var)
    ori_data = pd.read_excel(input_file, dtype=str)
    res_data = dataProcessServer(ori_data, output_file, weight_coe, price_coe)

