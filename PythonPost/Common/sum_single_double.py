class SumSingleDouble:
    def __init__(self):
        # 开奖数据
        self.data=[]
        self.post_list=[]
        self.sum_list=[]
        self.__direction=0
        self.__index=0
        self.__post_sum=0
        self.__sum=0
        
    def append(self,data):
        '''
        添加并计算一个数据
        '''
        self.data.append(data)
        
        if self.__index!=0:
            curr= 1 if data%2==1 else -1
            last= 1 if self.data[self.__index-1]%2==1 else -1
            mod_sum=curr+last
            if mod_sum!=0:
                self.__post_sum+=mod_sum/2

            if data%2==0:
                self.__direction_double=1
            else:
                self.__direction_double=-1

            self.__sum+=self.__direction_double*self.post_list[self.__index-1]


        self.post_list.append(self.__post_sum)
        self.sum_list.append(self.__sum)
        self.__index+=1
        
    def appends(self,datas):
        '''
        添加并计算一组数据
        '''
        for data in datas:
            self.append(data)