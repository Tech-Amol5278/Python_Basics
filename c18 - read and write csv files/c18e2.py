# Exercise: 
    # get the all the websites info in another file from given raw file
    # raw file : raw_website_info.txt

 ### using find ###
# with open('raw_website_info.txt') as rf:
#     with open('webs.txt','w') as  wf:
#         for line in rf.readlines():
#             if line.find('https'):
#                 print(line)

## using only IN operator
with open('raw_website_info.txt') as rf:
    with open('c18e2s2.txt','w') as wf:
        for line in rf.readlines():
            if 'https' in line:
                # print(line)
                # print(line.find('https'))
                wf.write(line[line.find('https'):-1] +  '\n')

# but above code has below limitation:
    # suppose a line has two URL's in that case this output will not be in two separate lines.

 
    