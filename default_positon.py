



class Default_position:

    def __init__(self):
        pass




    def stand_default_position(self,window,value):
        if int(window.get()) <int(value):
            window.delete(0)
            window.insert(0,'{}'.format(value))
            self.master.after(500,self.stand_default_position(window,value))
            print('1')
