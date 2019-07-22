





class Animatron:
    #instance class create when all values be takes from gui
    #and this appear in gui
    def __init__(self,speed):
        self.default_speed = speed
        self.begin_positions = [0,speed, 0,speed, 100,speed, 100,speed, 130,speed, 30,speed, 30,speed, 30,speed, 0,50]


    def create_model(self,num,over,shag,values):
        model ={str(i): values for i in range(int(num),int(over),int(shag))}
        return model

    def add_to_model(self,model):
        #insert values from gui
        #and here wanna possible realize 
        pass


    def create_frame(self):
        pass


    def complete_model_for_template():
        pass
