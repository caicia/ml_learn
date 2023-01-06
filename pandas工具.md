swifter 性能提升  
pivot_table  数据透视表  
shift  数据移动  
describe  数值型数据的描述性统计  
describe(include=np.object)  非数值型特征  
isnull().sum()  缺失值处理  
any(data.duplicated()) 检测数据是否存在重复值,结果为True则说明存在重复值,反之则不存在  
sns.boxplot(x='Churn',y='MonthlyCharges',data=data)  通过箱线图查看前面的数值型数据是否异常  
data['Churn'] = data['Churn'].map({'No':0,'Yes':1})  

# 数据标准化，转化为0,1
telcomvar = data.iloc[:,2:20]  
telcomvar.drop('PhoneService',axis=1,inplace=True)  
scaler = StandardScaler(copy=False)  
telcomvar[['tenure','MonthlyCharges','TotalCharges']] = scaler.fit_transform(telcomvar[['tenure','MonthlyCharges','TotalCharges']])  

# 使用sklearn标签编码，将分类数据转换为整数编码
def labelencode(col):  
    telcomvar[col] = LabelEncoder().fit_transform(telcomvar[col])  
for i in range(0,len(telcomobject.columns)):  
    labelencode(telcomobject.columns[i])  
for i in range(0,len(telcomobject.columns)):  
    uni(telcomobject.columns[i])  

# 相关系数  
players['Age'].corr(players['Rating'])  

# 根据年龄段来分组，统计每组年龄均值，用折线图描述年龄段和评分之间关系  
players['Age2'] =pd.cut(players['Age'],bins=4,labels=['少年队','青年队','成年队','老队'])  


# 还可以自定义区间范围  
pd.cut(players['Age'],bins=[10,16,22,33,45],labels=['少年队','青年队','成年队','老将队'])  

# 重复值查看  
data.duplicated().any()  

import matplotlib.pyplot as plt  
# 支持中文显示  
plt.rcParams['font.family']='Kaiti'  
# 使用非unicode的负号，当使用中文时候要设置  
plt.rcParams['axes.unicode_minus']=False  


# 重复值查看  
data.duplicated().any()  

