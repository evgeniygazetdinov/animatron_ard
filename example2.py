from subprocess import call
import shutil
from sketchbooks.SW.run_servo import compiling
from random import randint
import random
from collections import  OrderedDict

class EXAMPLER:
    def __init__(self):
        i=10
        self.default_begin = [0,50, 0,50, 100,50, 100,50, 130,50, 30,50, 30,50, 30,50, 0,50]
        self.servo_angles_defaults = [90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50]
        self.sql_time = 1




        self.duration = 18000


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





    def generateNumber(self,num,over,shag,values):
        model = {}
        for i in range(num,over,shag):
            model['{}'.format(i)] = values

        return model


    def division_angles(self,min_interval,interval_servo,angle_1,angle_2):
        # division angle depend on minimal interval
            division_angle = min_interval/interval_servo
            first_angle_for_execute  = division_angle/angle_1
            second_angle_for_execute  = division_angle/angle_2
            return first_angle_for_execute,second_angle_for_execute



    def create_intervals(self):
        my_randoms=[random.randrange(1,101,1) for _ in range (5)]
        return my_randoms


    def find_minimal_interval(self):
        my_intervals = self.create_intervals()
        min_interval = min(my_intervals)
        return min_interval




    def comprassion(self,time_execute,servo_scale,positon):
        # servo_scale meaning is scale for comprasion with  default scale in minimal interval
        # he obtain values from servo scale and changed yourself.if servo angle doesn't have position between
        for key in servo_scale.keys():
            # print(time_execute)
            # print("not changed" +str(time_execute[key][positon]))

            if time_execute[key] >= servo_scale[key]:
                time_execute[key][positon] = servo_scale[key][positon]
                # print('changed on'+ str(new_time_execute[key][positon]))
                # print(new_time_execute[key][positon])

    def create_min_keys(self):
        min_interval = self.find_minimal_interval()
        # create time scale with keys  and position
        # time_execute = [self.generateNumber(oldvalues.key,new_values.key,interval)]
        time_execute = [self.generateNumber(0,15,min_interval,self.default_begin)]
        print('time_execute is '+str(time_execute))
        return time_execute


    def create_some_servo_angles(self):
        servo_angle = self.generateNumber(0,10,5,self.servo_angles_defaults)
        print('servo execute is '+str(servo_angle))
        return servo_angle

    def create_execute(self):
        min_interval = self.create_min_keys()
        servo_angle = self.create_some_servo_angles()
        self.comprassion(min_interval,servo_angle,1)



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















caca = EXAMPLER()

caca.create_execute()
























############################################################################################################################################
