class SumSingleDouble:
    def __init__(self):
        # 开奖数据
        self.data=[]
        # 该期投注双结果
        self.__sum_double=0
        # 投注双走势
        self.sum_list_double=[]
        # 该期投注单结果
        self.__sum_single=0
        # 投注单走势
        self.sum_list_single=[]
        
        self.__direction_double=0
        self.__direction_single=0
        
    def append(self,data):
        '''
        添加并计算一个数据
        '''
        self.data.append(data)
        
        # 求单双差值（双）
        if data%2==0:
            self.__direction_double=1
        else:
            self.__direction_double=-1
        self.__sum_double+=self.__direction_double
        self.sum_list_double.append(self.__sum_double)
        
        # 求单双差值（单）
        if data%2==1:
            self.__direction_single=1
        else:
            self.__direction_single=-1
        self.__sum_single+=self.__direction_single
        self.sum_list_single.append(self.__sum_single)
        
    def appends(self,datas):
        '''
        添加并计算一组数据
        '''
        for data in datas:
            self.append(data)