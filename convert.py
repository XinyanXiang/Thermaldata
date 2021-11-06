import os
import csv

measurement_data = "measurement.csv"
channel_data = "channel.csv"

current_path = os.getcwd()
channel_folder_list = os.listdir(current_path)

channels_list = {}

channel_data_name = os.path.join(current_path, channel_data )
measurement_data_name = os.path.join(current_path, measurement_data)

with open(channel_data_name, 'w') as  channel_data_file:
     channel_data_writer = csv.writer(channel_data_file)
     channel_count = 0
     for folder in channel_folder_list:
          if folder.startswith('geo'): 
               channel_index = folder.index("_",35)
               channel_name = folder[channel_index+1]
               if channel_name not in channels_list:
                    channe_count = channel_count + 1
                    channels_list[channel_name] = channel_count
                    channel_data_writer.writerow([channe_count,channel_name])

channel_information_list = []
with open(channel_data_name, 'r') as channel_data_name_file:
     channel_data_name_reader = csv.reader(channel_data_name_file)
     for channel_row in channel_data_name_reader:
         channel_information_list.append(channel_row[1])
              


with open(measurement_data_name, 'w') as measurement_data_file:
     measurement_data_writer = csv.writer(measurement_data_file)
     for folder in channel_folder_list:
          if folder.startswith('geo'): 
               channel_index = folder.index("_",35)
               channel_name = folder[channel_index+1]
               channel_id = channel_information_list.index(channel_name) + 1
               file_path = current_path + "/{0}".format(folder)
               file_name_list = os.listdir(file_path)
               id_count = 0
               for file in file_name_list:
                    if file.endswith('.csv'):
                         id_count = id_count + 1
                         # file_format = file.replace(" ", "_")
                         new_file = "new" + file
                         file_local = os.path.join(file_path, file)
                         newfile_local = os.path.join(file_path, new_file)
                         with open(file_local,"r") as each_measurement_file:
                              with open(newfile_local,"w") as each_measurement_write_file:
                                   reader = csv.reader(each_measurement_file)
                                   writer = csv.writer(each_measurement_write_file)
                                   all = []
                                   row = next(reader)
                                   row.append('measurement_id')
                                   all.append(row)

                                   for row in reader:
                                        row.append(id_count)
                                        all.append(row)

                                   writer.writerows(all)
                         time_period_index = file.index("_",7)
                         time_period = file[time_period_index+1:-5]
                         measurement_data_writer.writerow([id_count,str(time_period),channel_id])
                         
                         
             



                    
