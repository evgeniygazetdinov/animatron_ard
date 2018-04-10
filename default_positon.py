



class Default_position:

    def __init__(self):
        pass




    def stand_default_position(self,window,value,sec_value):
            if int(window.get()) < int(value) or int(window.get()) > int(sec_value):
                window.delete(0, 'end')
                window.insert(0,'{}'.format(value))
                self.master.after(500,self.stand_default_position(window,value,sec_value))
        
