from subprocess import call
import shutil
from sketchbooks.SW.run_servo import compiling
from random import randint
import random
from collections import  OrderedDict
import  itertools
class EXAMPLER:
    def __init__(self):
        i=10
        self.default_begin = [0,50, 0,50, 100,50, 100,50, 130,50, 30,50, 30,50, 30,50, 0,50]
        self.servo_angles_defaults = [90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50]
        self.sql_time = 1
        self.duration = 18000
        self.counter  = 0
        # variable for save default keys quantity
        self.key = 84
        self.sql_speed1 = []
        self.sql_speed2 = []
        self.sql_speed3 = []
        self.sql_speed4 = []
        self.sql_speed5 = []
        self.sql_speed6 = []
        self.sql_speed7 = []
        self.sql_speed8 = []
        self.sql_speed9 = []
        self.sql_servo_1 = []
        self.sql_servo_2 = []
        self.sql_servo_3 = []
        self.sql_servo_4 = []
        self.sql_servo_5 = []
        self.sql_servo_6 = []
        self.sql_servo_7 = []
        self.sql_servo_8 = []
        self.sql_servo_9 = []
        self.time = []


    def switcher(self,f,s):
        return f,s

    def generateNumber(self,num,over,shag,values):
        # generate model execute for compare with servo execute
        model = {}
        for i in range(int(num),int(over),int(shag)):
            model['{}'.format(i)] = values

        return model



    def create_intervals(self):
        #obviously create list intervals of all servos
        my_randoms=[random.randrange(1,101,1) for _ in range (100)]
        return my_randoms


    def find_minimal_interval(self,interval):
        # compare all intervals
        my_intervals = interval
        min_interval = min(my_intervals)
        return min_interval


    def create_min_keys(self):
        min_interval = 0.2
        time_execute = self.generateNumber(0,80,1,self.default_begin)
        return time_execute


    def create_some_servo_angles(self):
        # generate servo execute list
        servo_angle = self.generateNumber(0,10,5,self.servo_angles_defaults)
        return servo_angle


    def call_just_one_angle(self,one_angle,another_angle):
        # return one value by counter
        # fix just one TODO
        self.counter +=1
        if self.counter == 1:
            self.counter+1
            return one_angle
        if self.counter == 2:
            self.counter = 0
            return another_angle



    def keys_finder(self):
        # first place for global values
        self.key = len(self.create_min_keys())
        print('HUEC'+(str(len(self.create_min_keys()))))


    def single_repeater(self,angle_for_repeat,key_number):
        # just return quantity angles (more important quantity)
        some_execute = []
        for _ in range(key_number):
            some_execute.append(angle_for_repeat)
        return some_execute

    def divider_angle(self,basic_angle,min,interval_servo,
                      begin_divider,key_number):
        # get in angle for divide,min interval,interval servo,
        # number from which begin divide,and quantity key for divide
        min_interval = min
        interval_servo = interval_servo
        interval_div = int((interval_servo * 10) / (min_interval * 10))
        div_angle = begin_divider
        interval = int(basic_angle / interval_div)
        some_execute = [div_angle]
        for _ in range(key_number):
            div_angle += interval
            if div_angle > basic_angle:
                interval *= -1
                div_angle += interval
                continue
            if div_angle < 0:
                interval *= -1
                div_angle += interval
                continue
            some_execute.append(div_angle)


        return some_execute

    def limiter_for_switcher(self,loop,keys):
        # this func need for right quantity values from exiting from loop
        # she add or delete excess digit from list
        while len(loop) != keys:
            if len(loop) > keys:
                del loop[-1]
                if len(loop) == keys:
                    break
            if len(loop) <  keys:
                for item in loop:
                    loop.append(int(loop[item]))
                    # if item :
                    #     item/2
                    if len(loop) == keys:
                        break
            print(len(loop))
            return loop








    def switcher(self,first_angle,second_angle,min,interval_servo,
                 begin_divider,key_number):
        loop = []
        total_loop = []
        # this func must be change angle passing just one  loop with quantity keys
        # this stuff be responsibility by loop
        # in my mind just one sequence divide angle after she begin anothe with another angle
        # for example first angle 180 begin by 20 and interval =10 second angle 60 begin by 20 and interval 5
        # 20 30 40 50 60 70 80 90  etc 180 170 160 150 etc 20 25 30 35 etc 60 55 50 45 40 35 30 25 20  etc 180
        # simple implementation is divider angle launched 2
        loop.append(self.divider_angle(first_angle,min,interval_servo,
                          begin_divider,key_number))

        loop.append(self.divider_angle(second_angle,min,interval_servo,
                          begin_divider,key_number))
        # this place for merging to list in one
        for i in loop:
            total_loop += i
        print(total_loop)

        # # TODO rebuld divider angle output 'he has wrong structure'
        final_loop = self.limiter_for_switcher(total_loop,key_number)
        return final_loop
            # rebuild stuff in side 2divider angle create common list with values.lenght this list depend on quantity keys
            # after return list with values .Which is will add on commom scale with minamal interval.



    def selector(self,loop,basic_angle,min,interval_servo,
                      begin_divider,key_number):
        # choose prefer method put values on scale_with_interval
        if loop == True:
            switcher(first_angle,second_angle,min,interval_servo,
                         begin_divider,key_number)
        else:
            single_repeater(basic_angle,min,interval_servo,key_number)



    def comparer_two_list(self,first_serif,second_serif,):
        # this func must be return begins and over for divider_angle
        for serif in first_serif:
            if serif in second_serif:
                pass


    def servo_on_min_interval(self,execute,number,number_1,number_2,
                              number_3,number_4,number_5,
                              number_6,number_7,number_8,
                              position,position_1,position_2,
                              position_3,position_4,position_5,
                              position_6,position_7,position_8):
        # big staff loop for insert values in keys
       execution = execute
       servo_execute = self.selector(number)
       servo_execute1 = self.selector(number_1)
       servo_execute2 = self.selector(number_2)
       servo_execute3 = self.selector(number_3)
       servo_execute4 = self.selector(number_4)
       servo_execute5 = self.selector(number_5)
       servo_execute6 = self.selector(number_6)
       servo_execute7 = self.selector(number_7)
       servo_execute8 = self.selector(number_8)

       for i, key in enumerate(execution):
           execution[key][position] = servo_execute[i]
           execution[key][position_1] = servo_execute1[i]
           execution[key][position_2] = servo_execute2[i]
           execution[key][position_3] = servo_execute3[i]
           execution[key][position_4] = servo_execute4[i]
           execution[key][position_5] = servo_execute5[i]
           execution[key][position_6] = servo_execute6[i]
           execution[key][position_7] = servo_execute7[i]
           execution[key][position_8] = servo_execute8[i]
           print([key],position,i)
       return execution


    def big_while(self):

        scale = self.create_execute()
        print(scale)
        return scale3

    def use_execute(self):
        execute = self.servo_on_min_interval(198,91,92,
                                  93,94,95,
                                  96,97,98,
                                  0,2,4,6,
                                  8,10,12,
                                  14,1)
        for key,values  in execute.items():
            print(str(key),str(values)+'\n')

        for key,value in execute.items():
            self.sql_speed1.append(value[1])
            self.sql_speed2.append(value[3])
            self.sql_speed3.append(value[5])
            self.sql_speed4.append(value[7])
            self.sql_speed5.append(value[9])
            self.sql_speed6.append(value[11])
            self.sql_speed7.append(value[13])
            self.sql_speed8.append(value[15])
            self.sql_speed9.append(value[17])
            self.sql_servo_1.append(value[0])
            self.sql_servo_2.append(value[2])
            self.sql_servo_3.append(value[4])
            self.sql_servo_4.append(value[6])
            self.sql_servo_5.append(value[8])
            self.sql_servo_6.append(value[10])
            self.sql_servo_7.append(value[12])
            self.sql_servo_8.append(value[14])
            self.sql_servo_9.append(value[16])
            self.time.append(key)


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
            line = line.replace(",'", ',')
            line = line.replace("{'", '{')
            line = line.replace("'};", " };")
            line = line.replace("', '", ' , ')

            o.write(line)
        o.close()



    def writing(self):
        self.use_execute()
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


loop = [i for i in range(20)]
# xaxa =  EXAMPLER()
# print(xaxa.switcher(44,99,0.1,0.4,
#              20,99))
