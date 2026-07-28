data =[
        ['01', '001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyo'],
        ['01', '002' , 'Male' , 'Sato' , 'Takashi' , 27 , 'Kanagawa'],
        ['01', '003' , 'Female' , 'Tanaka' , 'YUko' , 25, 'Saitama'],
        ['02', '001' , 'Male' , 'Smith' , 'Mike' , 22 , 'NewJersey'],
        ['02', '002' , 'Male' , 'Turner' , 'Tom' , 27 , 'Kansas'],
        ['02', '003' , 'Male' , 'Jackson' ,'David' , 22 , 'Florida']
        ]
data

member_information = {}

for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info

print('number', 'information', sep='\t')
for key, info in member_information.items():
    print(key, info)
