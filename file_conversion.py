#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


c_genes = ['p53', 'akt1', 'bcl2', 'cd274', 'ctnnb1', 'egfr', 'erbb2', 'esr1', 'ewsr1', 'fgfr3', 'mdm2', 'myc', 'mycn', 'numa1',
          'runx2', 'usp7']
nc_genes = ['atad2', 'bnip1', 'cpne3', 'epb41', 'gapdh', 'gprc5a', 'hrk', 'sema4c', 'znf653', 'zyve28']


# In[ ]:


# Python program to convert .tsv file to .csv file
# importing re library
import re
 
# reading given tsv file
for f_name in c_genes:
    with open(f_name+".tsv", 'r') as myfile: 
        with open(f_name+"_1.csv", 'w') as csv_file:
            for line in myfile:
       
      # Replace every tab with comma
                fileContent = re.sub("\t", ",", line)
       
      # Writing into csv file
                csv_file.write(fileContent)
            csv_file.close()
        myfile.close()
 
# output
print("Successfully made csv files")


# In[ ]:


for f_name in nc_genes:
    with open("non cancer/"+f_name+".tsv", 'r') as myfile: 
        with open(f_name+"_1.csv", 'w') as csv_file:
            for line in myfile:
       
      # Replace every tab with comma
                fileContent = re.sub("\t", ",", line)
       
      # Writing into csv file
                csv_file.write(fileContent)
            csv_file.close()
        myfile.close()
 
# output
print("Successfully made csv files")

