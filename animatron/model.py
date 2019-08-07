
from collections import deque
from collections import OrderedDict



class Model:
    #instance class create when all values be takes from gui
    #and this appear in gui
    def __init__(self,speed = 1):
        self.default_speed = speed
        self.begin_positions = [0, 0, 100, 100, 130, 30, 30, 30, 0,]
        self.default_time =50
        self.frame = deque()
    """
    def create_sketch(self,num,over,shag,values = self.begin_positions):
        model  = OrderedDict()
        for i in range(num,over,shag):
            model[str(i)] = values
        return model
    """
    def into_frame(self,model):
        #insert values from gui
        #self.create_sketch(num,over,shag)
        #self.frame.append(model)
        pass


    def conclusion_from_frame(self):
        self.frame.pop()


    def create_template(self):
        pass



if __name__ == "__main__" :
    base = Model()

