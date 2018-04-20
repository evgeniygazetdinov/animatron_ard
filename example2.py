from subprocess import call
import shutil
from sketchbooks.SW.run_servo import compiling

class EXAMPLER:
    def __init__(self):
        i=10
        self.default_begin = [0,50, 0,50, 100,50, 100,50, 130,50, 30,50, 30,50, 30,50, 0,50]
        self.sql_time = 1
        nu1=90
        nu2=90
        nu3=90
        nu4=90
        nu5=50
        nu6=50
        nu7=90
        nu8=90
        nu9=90
        nu10=100
        nu11=100
        nu12=120
        nu13=130
        nu14=90
        nu15=90
        nu16=90
        nu17=90
        nu18=90
        nu19 = 90
        self.sql_speed3 = [nu1 for i in range(90)]
        self.sql_speed4 = [nu2 for i in range(90)]
        self.sql_speed5 = [nu3 for i in range(90)]
        self.sql_speed6 = [nu4 for i in range(90)]
        self.sql_speed7 = [nu5 for i in range(90)]
        self.sql_speed8 = [nu6 for i in range(90)]
        self.sql_speed9 = [nu7 for i in range(90)]
        self.sql_servo_1 = [self.switcher(180,90) for i in range(45)]
        self.sql_servo_2 = [self.switcher(180,90) for i in range(45)]
        self.sql_servo_3 = [self.switcher(110,100) for i in range(45)]
        self.sql_servo_4 = [nu12 for i in range(90)]
        self.sql_servo_5 = [nu13 for i in range(90)]
        self.sql_servo_6 = [nu14 for i in range(90)]
        self.sql_servo_7 = [self.switcher(90,30) for i in range(45)]
        self.sql_servo_8 = [self.switcher(30,90) for i in range(45)]
        self.sql_servo_9 = [nu17 for i in range(90)]
        self.sql_speed1 = [nu18 for i in range(90)]
        self.sql_speed2 = [nu19 for i in range(90)]

        self.time = self.generateNumber(0,18803,500),


        self.duration = 18000





    #
    # def time_on_swith(self,execute,interval):
    #     execute/interval = keys
    #     return keys
    #     pass



    def create_values(self):
        values = {self.time_slider.get():[servo_1.get(),servo_2.get(),
                                              servo_3.get(),servo_4.get(),
                                              servo_5.get(),servo_6.get(),
                                              servo_7.get(),servo_8.get(),
                                              servo_9.get()]}
        return values








    def time_finder(self):
        # find difference between oldvalues keys and new ,return time execute inter
        pass

    def interval_devider(min_interval,interval_servo,angle_1,angle_2):
        round(interval_servo)
        pass




    def values_on_keys(self):
        # return all keys to model with interval
        execute = time_finder()

    def interval_comparer(self):
        # comprases all interval and return most tiny
        pass


    def inter(self,old_values,new_values):
        old_values = create_values()
        first_point = old_values
        new_values = create_values()
        second_point = new_values
        intervals_comprasion(*intervals)
        keys_creating(min_interval,time)
        values_on_keys(first_point,second_point,values,keys)





    def switcher(self,f,s):
        return f,s




    def clear_strings(self):
        # clean by rubish
        f = open('template.h', 'r')
        o = open('VAL.h', 'w')
        print('writing1')
        while 1:
            line = f.readline()
            if not line: break
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',,', ',')
            line = line.replace("''", '0')
            line = line.replace('[][]', '[]')
            line = line.replace('{[]}', '{}')
            line = line.replace('{[', '{')
            line = line.replace(']}', '}')
            line = line.replace(')]};', '')
            o.write(line)
        o.close()



    def generateNumber(self,num,over,shag):
        model = {}
        for i in range(num,over,shag):
            model['{}'.format(i)] = self.default_begin

        return model

    def create_min_keys(self,min_interval):
        # create time scale with keys  and position
        # time_execute = [self.generateNumber(oldvalues.key,new_values.key,interval)]
        time_execute = [self.generateNumber(0,20000,min_interval)]
        return time_execute


    def create_servo_keys(self,min_interval):
        pass



    def division_angles(self,min_interval,interval_servo,angle_1,angle_2):
        # division angle depend on minimal interval
            division_angle = min_interval/interval_servo
            first_angle_for_execute  = division_angle/angle_1
            second_angle_for_execute  = division_angle/angle_2
            return first_angle_for_execute,second_angle_for_execute

    def comprassion(self,time_execute,servo_scale):
        for key in servo_scale.keys():
            if key in time_execute.keys():
                self.division_angles(2,3,90,0)








        # find similar keys and if find he changed,with
        # # func take min_values,servos_keys and compassion with some servos keys keys for yourself if he find something he changed min_values
        # crucial = {'eggs': '999','ham': '','cheese': '34'}
        # # dishes = {'eggs': [2,435,35,77,33,64], 'sausage': 1, 'bacon': 1, 'spam': 500}
        # for key in crucial.keys():
        #     if key in dishes.keys():
        #         # division_angles()
        #         dishes['eggs'][-1]=43
        #         print(dishes)










    def writing(self):
        with open('template.h', 'w') as file:
            file.writelines('int time_play={};\n'.format(self.duration))
            file.writelines('int speed_row[] = {')
            file.writelines(str(self.sql_speed1))
            file.writelines('};\n')
            file.writelines('int speed_row2[] = {')
            file.writelines(str(self.sql_speed2))
            file.writelines('};\n')
            file.writelines('int speed_row3[] = {')
            file.writelines(str(self.sql_speed3))
            file.writelines('};\n')
            file.writelines('int speed_row4[] = {')
            file.writelines(str(self.sql_speed4))
            file.writelines('};\n')
            file.writelines('int speed_row5[] = {')
            file.writelines(str(self.sql_speed5))
            file.writelines('};\n')
            file.writelines('int speed_row6[] = {')
            file.writelines(str(self.sql_speed6))
            file.writelines('};\n')
            file.writelines('int speed_row7[] = {')
            file.writelines(str(self.sql_speed7))
            file.writelines('};\n')
            file.writelines('int speed_row8[] = {')
            file.writelines(str(self.sql_speed8))
            file.writelines('};\n')
            file.writelines('int speed_row9[] = {')
            file.writelines(str(self.sql_speed9))
            file.writelines('};\n')
            file.writelines('int LEyeArray[][] = {')
            file.writelines(str(self.sql_servo_1))
            file.writelines('};\n')
            file.writelines('int REyeArray[] = {')
            file.writelines(str(self.sql_servo_2))
            file.writelines('};\n')
            file.writelines('int LArmArray[] = {')
            file.writelines(str(self.sql_servo_3))
            file.writelines('};\n')
            file.writelines('int RArmArray[] = {')
            file.writelines(str(self.sql_servo_4))
            file.writelines('};\n')
            file.writelines('int LhandArray[] = {')
            file.writelines(str(self.sql_servo_5))
            file.writelines('};\n')
            file.writelines('int RhandArray[] = {')
            file.writelines(str(self.sql_servo_6))
            file.writelines('};\n')
            file.writelines('int LLegArray[] = {')
            file.writelines(str(self.sql_servo_7))
            file.writelines('};\n')
            file.writelines('int RLegArray[] = {')
            file.writelines(str(self.sql_servo_8))
            file.writelines('};\n')
            file.writelines('int AssArray[] = {')
            file.writelines(str(self.sql_servo_9))
            file.writelines('};\n')
            file.writelines('unsigned long KeyArray[] = {')
            file.writelines(str(self.time))
            file.writelines('};\n')
        print('write to file')
        self.clear_strings()
        call('rm template.h', shell=True)
        shutil.move("/home/qbc/PycharmProjects/ard/VAL.h",
                    "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")



caca =  EXAMPLER()
# caca.writing()
# compiling()





















# caca.create_min_keys(2)
caca.comprassion()



















############################################################################################################################################
